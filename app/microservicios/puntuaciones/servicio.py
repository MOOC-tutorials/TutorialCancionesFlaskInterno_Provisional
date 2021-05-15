from flask import Flask, request
from flask_restful import Api, Resource
import requests
import json
import http


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
        req = requests.post('http://127.0.0.1:5002/tablaPuntajes/registrarPuntaje', json=cancion)
        
        return req.status_code


api.add_resource(VistaPuntuacion, '/cancion/<int:id_cancion>/puntuar')

if __name__ == '__main__':
    app.run(debug=True, port=5001)