from flask import Flask, request
from flask_restful import Api, Resource
import urllib
import json


app = Flask(__name__)
api = Api(app)

class VistaPuntuacion(Resource):

    def post(self, id_cancion):
        content = urllib.request.urlopen('http://127.0.0.1:5000/cancion/{}'.format(id_cancion)).read().decode('utf-8')
        cancion = json.loads(content)
        cancion["puntaje"] = request.json["puntaje"]
        cancion["review"] = request.json["review"]
        return cancion


api.add_resource(VistaPuntuacion, '/cancion/<int:id_cancion>/puntuar')

if __name__ == '__main__':
    app.run(debug=True, port=5001)