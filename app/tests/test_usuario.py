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
        self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        with app.app_context():
            self.assertEqual(len(Usuario.query.all()),1)

    def test_ver_usuario(self):
        self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        res = self.client.get('/usuario/1')
        album = json.loads(res.data)
        with self.app.app_context():
            self.assertEqual(album["nombre"], 'user')
            self.assertEqual(album["contrasena"], '12345')

    def test_eliminar_usuario(self):
        self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        self.client.delete('/usuario/1')
        res = self.client.get('/usuario/1')
        with self.app.app_context():
            self.assertEqual(res.status_code, 404)

    def test_editar_usuario(self):
        self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        self.client.put('/usuario/1', data=json.dumps(dict(nombre='user1234', contrasena='54321')), content_type='application/json')
        res = self.client.get('/usuario/1')
        usuario = json.loads(res.data)
        with self.app.app_context():
            self.assertEqual(usuario["nombre"], 'user')
            self.assertEqual(usuario["contrasena"], '54321')

    def test_crear_album_a_usuario(self):
        self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        res = self.client.post('/usuario/1/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CD')), content_type='application/json')
       
        with self.app.app_context():
            self.assertEqual(len(Album.query.all()), 1)
            album_agregado = Album.query.filter(Album.titulo == "prueba").first()
            self.assertIsNotNone(album_agregado)

    def test_crear_album_repetido_a_usuario(self):
        self.client.post('/login', data=json.dumps(dict(nombre='user', contrasena='12345')), content_type='application/json')
        res = self.client.post('/usuario/1/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CD')), content_type='application/json')
        res = self.client.post('/usuario/1/albumes', data=json.dumps(dict(titulo='prueba', anio='2000', descripcion='na', medio='CD')), content_type='application/json')
        with self.app.app_context():
            self.assertEqual(len(Album.query.all()), 2)
            album_agregado = Album.query.filter(Album.titulo == "prueba").first()
            self.assertIsNotNone(album_agregado)
