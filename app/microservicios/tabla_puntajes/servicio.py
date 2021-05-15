from app import create_app, db, api
from modelos.modelos import Cancion, CancionSchema
from tareas import registrar_puntaje
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import urllib

cancion_schema = CancionSchema()

class VistaRegistrarPuntajes(Resource):

    def post(self):
        registrar_puntaje.delay(request.json)
        return '',204
        

class VistaTablaPuntaje(Resource):

    def get(self):
        return [cancion_schema.dump(ca) for ca in Cancion.query.all()]

api.add_resource(VistaRegistrarPuntajes, '/tablaPuntajes/registrarPuntaje')
api.add_resource(VistaTablaPuntaje, '/tablaPuntajes')


app = create_app('default')
app_context = app.app_context()
app_context.push()


db.create_all()

if __name__ == '__main__':
    app.run(debug = True, port=5002)