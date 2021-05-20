from flask import Flask, request
from flask_restful import Api, Resource
import requests
import json
import http
from celery import Celery

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task(name="tabla.registrar")
def registrar_puntaje(cancion_json):
    pass

app = Flask(__name__)
api = Api(app)


class VistaPuntuacion(Resource):

    def post(self, id_cancion):
        content = requests.get('http://127.0.0.1:5000/cancion/{}'.format(id_cancion))
        
        cancion = content.json()
        cancion["puntaje"] = request.json["puntaje"]
        cancion["review"] = request.json["review"]
        #data = urllib.parse.urlencode(cancion).encode()
        print(json.dumps(cancion))
        #req = requests.post('http://127.0.0.1:5002/tablaPuntajes/registrarPuntaje', json=cancion)
        args = (cancion,)
        registrar_puntaje.apply_async(args, queue='tabla', serializer='json')
        

        return '',202


api.add_resource(VistaPuntuacion, '/cancion/<int:id_cancion>/puntuar')

if __name__ == '__main__':
    app.run(debug=True, port=5001)