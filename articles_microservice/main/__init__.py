import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_caching import Cache
from consulate import Consul
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

             , "traefik.http.services.article.loadbalancer.server.scheme=http"] 
    )

    keyarticles = consul.kv
    app.config['CACHE_TYPE'] = keyarticles["articles/CACHE_TYPE"] #os.getenv("CACHE_TYPE")
    app.config['CACHE_DEFAULT_TIMEOUT'] = keyarticles["articles/CACHE_DEFAULT_TIMEOUT"] #os.getenv("CACHE_DEFAULT_TIMEOUT")
    app.config['CACHE_REDIS_PASSWORD'] = keyarticles["articles/CACHE_REDIS_PASSWORD"] #os.getenv("CACHE_REDIS_PASSWORD")
    app.config['CACHE_REDIS_URL'] = f'redis://{keyarticles["articles/CACHE_REDIS_HOST"]}:{keyarticles["articles/CACHE_REDIS_PORT"]}/{keyarticles["articles/CACHE_REDIS_DB"]}'
    #f'redis://{os.getenv("CACHE_REDIS_HOST")}:{os.getenv("CACHE_REDIS_PORT")}/{os.getenv("CACHE_REDIS_DB")}'
    cache.init_app(app)
    HOST = keyarticles["articles/DB_HOST"]           #os.getenv("DB_HOST") 
    USER = keyarticles["articles/DB_USER"]           #os.getenv("DB_USER")
    PASSWORD = keyarticles["articles/DB_PASSWORD"]   #os.getenv("DB_PASSWORD")
    PORT = keyarticles["articles/DB_PORT"]           #os.getenv("DB_PORT")
    DB_NAME = keyarticles["articles/DB_DATABASE"]    #os.getenv("DB_DATABASE")

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