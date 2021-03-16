import flask_unittest
from app import app
from modelos.modelos import *
import unittest
import json

class test_cancion(unittest.TestCase):

    def create_app(self):
        pass

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            # Crea las tablas de la base de datos
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.remove()
            db.drop_all()

    def test_crear_cancion(self):
        res = self.client.post('/canciones', data=json.dumps(dict(titulo='prueba', minutos='3', segundos='15', interprete='Aterciopelados')), content_type='application/json')
       
        with self.app.app_context():
            self.assertEqual(len(Cancion.query.all()), 1)
            cancion_agregada = Cancion.query.filter(Cancion.titulo == "prueba").first()
            self.assertIsNotNone(cancion_agregada)

    def test_ver_canciones(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='3', segundos='30', interprete="músico 1")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba2',  minutos='3', segundos='30', interprete="músico 2")), content_type='application/json')
        res = self.client.get('/canciones')

        with self.app.app_context():
            self.assertEqual(len(json.loads(res.data)), 2)