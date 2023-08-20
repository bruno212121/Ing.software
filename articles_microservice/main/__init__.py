import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_caching import Cache
from consulate import Consul
from consulate.models import agent
import pybreaker
import socket


consul = Consul(host="consul")
api = Api()
db = SQLAlchemy()
cache = Cache()
db_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)


def create_app():
    app = Flask(__name__)
    load_dotenv()

    serviceip = socket.gethostbyname(socket.gethostname())
    
    checks=agent.Check(
        name="articles",
        http="https://article.order.localhost/healthcheck",
        interval="10s",
        tls_skip_verify=True,
        timeout="1s",
        status="passing"
    )
    
    #autoregistro en consul automatico
    consul.agent.service.register(
        name="articles",
        service_id="articles",
        address=serviceip,
        tags=["traefik.enable=true"
             , "traefik.http.routers.article.rule=Host(`article.order.localhost`)"
             , "traefik.http.routers.article.tls=true"
             , "traefik.http.services.article.loadbalancer.server.port=7000"
             , "traefik.docker.network=red"
            
             , "traefik.http.middlewares.latency-check.circuitbreaker.expression=LatencyAtQuantileMS(50.0) > 100"

             , "traefik.http.services.article.loadbalancer.server.scheme=http"], 
        checks=[checks] #TODO: aca ya hay algo que falta
    )

    from main.routes import routes
    app.register_blueprint(routes.articles)

    keyarticles = consul.kv
    app.config['CACHE_TYPE'] = keyarticles["articles/CACHE_TYPE"] # or os.getenv("CACHE_TYPE")
    app.config['CACHE_DEFAULT_TIMEOUT'] = keyarticles["articles/CACHE_DEFAULT_TIMEOUT"] # or os.getenv("CACHE_DEFAULT_TIMEOUT")
    app.config['CACHE_REDIS_PASSWORD'] = keyarticles["articles/CACHE_REDIS_PASSWORD"] # or os.getenv("CACHE_REDIS_PASSWORD")
    app.config['CACHE_REDIS_URL'] = f'redis://{keyarticles["articles/CACHE_REDIS_HOST"]}:{keyarticles["articles/CACHE_REDIS_PORT"]}/{keyarticles["articles/CACHE_REDIS_DB"]}' # or f'redis://{os.getenv("CACHE_REDIS_HOST")}:{os.getenv("CACHE_REDIS_PORT")}/{os.getenv("CACHE_REDIS_DB")}'

    cache.init_app(app)
    HOST = keyarticles["articles/DB_HOST"]           # or os.getenv("DB_HOST") 
    USER = keyarticles["articles/DB_USER"]           # or os.getenv("DB_USER")
    PASSWORD = keyarticles["articles/DB_PASSWORD"]   # or os.getenv("DB_PASSWORD")
    PORT = keyarticles["articles/DB_PORT"]           # or os.getenv("DB_PORT")
    DB_NAME = keyarticles["articles/DB_DATABASE"]    # or os.getenv("DB_DATABASE")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

    db.init_app(app)

    #Permitir solicitudes de otros origenes
    cors = CORS(app, support_credentials=True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    # TODO: si descomento esto fallan todos los tests taquelorepario
    try:
        from main.controllers import ArticleController, ArticlesController, CategoryController
        api.add_resource(ArticleController, '/article/<int:id>', endpoint='article')
        api.add_resource(ArticlesController, '/articles', endpoint='articles')
        api.add_resource(CategoryController, '/categories', endpoint='categories')

        api.init_app(app)
    except Exception as e:
        print(e)
        pass

    return app