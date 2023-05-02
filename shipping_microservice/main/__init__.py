import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask_restful import Api
from flask_cors import CORS

api = Api()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    HOST = os.getenv("DB_HOST")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_DATABASE")
    VIRTUAL_HOST = os.getenv("VIRTUAL_HOST")
    ARTICLE_API = os.getenv("ARTICLE_API")

    print(f'HOST: {HOST}')
    print(f'USER: {USER}')
    print(f'PASSWORD: {PASSWORD}')
    print(f'PORT: {PORT}')
    print(f'DB_NAME: {DB_NAME}')
    print(f'VIRTUAL_HOST: {VIRTUAL_HOST}')
    print(f'ARTICLE_API: {ARTICLE_API}')


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

    db.init_app(app)

    #Permitir solicitudes de otros origenes
    cors = CORS(app, support_credentials=True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"*": {"origins": "*"}})

    try:

        from main.controllers import ShipController, ArticlesOrderController, OrderController, SucursalController, ArticlesController
        api.add_resource(OrderController, '/orders', endpoint='orders')
        api.add_resource(ArticlesOrderController, '/articlesorders', endpoint='articlesorders')
        api.add_resource(SucursalController, '/sucursales', endpoint='sucursales')
        api.add_resource(ArticlesController, '/articles', endpoint='articles')
        api.add_resource(ShipController, '/ships', endpoint='ships')
        api.init_app(app)

        from main.services import order_api
        app.register_blueprint(order_api, url_prefix='/order_api')

    except Exception as e:
        print(e)
        pass

    return app