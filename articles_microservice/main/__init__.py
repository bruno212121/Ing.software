import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()


    HOST = os.getenv("DB_HOST")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    PORT = int(os.getenv("DB_PORT"))
    DB_NAME = os.getenv("DB_DATABASE")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

    db.init_app(app)

    return app