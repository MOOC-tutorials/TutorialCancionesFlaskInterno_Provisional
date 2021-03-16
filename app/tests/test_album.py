import flask_unittest
from app import app
from modelos.modelos import *
import unittest
import json

class test_album(unittest.TestCase):

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

    def test_crear_album(self):
        res = self.client.post('/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CD')), content_type='application/json')
       
        with self.app.app_context():
            self.assertEqual(len(Album.query.all()), 1)
            album_agregado = Album.query.filter(Album.titulo == "prueba").first()
            self.assertIsNotNone(album_agregado)
            
    def test_ver_albumes(self):
        self.client.post('/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CD')), content_type='application/json')
        self.client.post('/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CASETE')), content_type='application/json')
        res = self.client.get('/albumes')

        with self.app.app_context():
            self.assertEqual(len(json.loads(res.data)), 2)

    def test_ver_album_no_existente(self):
        res = self.client.get('/album/1')
        with self.app.app_context():
            self.assertEqual(res.status_code, 404)

    def test_ver_album_no_existente(self):
        self.client.post('/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CD')), content_type='application/json')
        res = self.client.get('/album/1')
        album = json.loads(res.data)
        with self.app.app_context():
            self.assertEqual(album["titulo"], 'prueba')
            self.assertEqual(album["anio"], 1999)
            self.assertEqual(album["descripcion"], 'na')
            self.assertEqual(album["medio"]['llave'], 'CD')

    def test_editar_album(self):
        self.client.post('/albumes', data=json.dumps(dict(titulo='prueba', anio='1999', descripcion='na', medio='CD')), content_type='application/json')
        self.client.put('/album/1', data=json.dumps(dict(titulo='prueba2', anio='2000', descripcion='blablabla', medio='CASETE')), content_type='application/json')
        res = self.client.get('/album/1')
        album = json.loads(res.data)
        with self.app.app_context():
            self.assertEqual(album["titulo"], 'prueba2')
            self.assertEqual(album["anio"], 2000)
            self.assertEqual(album["descripcion"], 'blablabla')
            self.assertEqual(album["medio"]['llave'], 'CASETE')



    