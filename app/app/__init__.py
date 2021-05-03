from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()
celery = Celery(__name__, broker='redis://localhost:6379/0', include=['tareas'])

def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    db.init_app(app)
    api.init_app(app)
    celery.config_from_object(app.config)
    return app