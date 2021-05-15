from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

db = SQLAlchemy()
api = Api()
celery = Celery(__name__, broker='redis://localhost:6379/0')

def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://estudiante:12345@localhost:5432/tabla'
    db.init_app(app)
    api.init_app(app)
    return app
