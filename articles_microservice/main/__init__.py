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

    # print(f'HOST: {HOST}')
    # print(f'USER: {USER}')
    # print(f'PASSWORD: {PASSWORD}')
    # print(f'PORT: {PORT}')
    # print(f'DB_NAME: {DB_NAME}')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

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