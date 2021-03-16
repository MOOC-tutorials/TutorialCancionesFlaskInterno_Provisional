import flask_unittest
from app import app
from modelos.modelos import *
import unittest
import json

class test_usuario(unittest.TestCase):

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

    def test_crear_usuario(self):
        res = self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        with app.app_context():
            self.assertEqual(len(Usuario.query.all()),1)

