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
    
    def test_ver_cancion(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='3', segundos='30', interprete="músico 1")), content_type='application/json')
        res = self.client.get('/cancion/1')
        cancion = json.loads(res.data)
        with self.app.app_context():
            self.assertEqual(cancion["titulo"], 'prueba1')
            self.assertEqual(cancion["minutos"], 3)
            self.assertEqual(cancion["segundos"], 30)
            self.assertEqual(cancion["interprete"], 'músico 1')

    def test_editar_cancion(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='3', segundos='30', interprete="músico 1")), content_type='application/json')
        self.client.put('/cancion/1', data=json.dumps(dict(titulo='prueba modificada', minutos='1', segundos='50', interprete="músico 2")), content_type='application/json')
        res = self.client.get('/cancion/1')
        cancion = json.loads(res.data)
        with self.app.app_context():
            self.assertEqual(cancion["titulo"], 'prueba modificada')
            self.assertEqual(cancion["minutos"], 1)
            self.assertEqual(cancion["segundos"], 50)
            self.assertEqual(cancion["interprete"], 'músico 2')
            
    def test_eliminar_cancion(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='3', segundos='30', interprete="músico 1")), content_type='application/json')
        self.client.delete('/cancion/1')
        res = self.client.get('/cancion/1')
        with self.app.app_context():
            self.assertEqual(res.status_code, 404)
    
    def test_buscar_cancion_sin_parametros(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='3', segundos='30', interprete="músico 1")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba2',  minutos='3', segundos='30', interprete="músico 2")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba3',  minutos='3', segundos='30', interprete="músico 3")), content_type='application/json')
        res = self.client.get('/canciones?nombre')
        with self.app.app_context():
            self.assertEqual(len(json.loads(res.data)), 3)

    def test_buscar_cancion_coincidencia_exacta(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='1', segundos='20', interprete="músico 1")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba2',  minutos='2', segundos='30', interprete="músico 2")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba3',  minutos='3', segundos='40', interprete="músico 3")), content_type='application/json')
        res = self.client.get('/canciones?nombre=prueba1')
        with self.app.app_context():
            canciones = json.loads(res.data)
            self.assertEqual(len(canciones), 1)
            self.assertEqual(canciones[0]["titulo"],"prueba1")
            self.assertEqual(canciones[0]["minutos"],1)
            self.assertEqual(canciones[0]["segundos"],20)
            self.assertEqual(canciones[0]["interprete"],"músico 1")

    def test_buscar_cancion_coincidencia_parcial(self):
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba1', minutos='1', segundos='20', interprete="músico 1")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba2',  minutos='2', segundos='30', interprete="músico 2")), content_type='application/json')
        self.client.post('/canciones', data=json.dumps(dict(titulo='prueba3',  minutos='3', segundos='40', interprete="músico 3")), content_type='application/json')
        res_1 = self.client.get('/canciones?nombre=prueba')
        res_2 = self.client.get('/canciones?nombre=2')
        with self.app.app_context():
            canciones_1 = json.loads(res_1.data)
            self.assertEqual(len(canciones_1), 3)
            self.assertEqual(canciones_1[0]["titulo"],"prueba1")
            self.assertEqual(canciones_1[1]["titulo"],"prueba2")
            self.assertEqual(canciones_1[2]["titulo"],"prueba3")
            canciones_2 = json.loads(res_2.data)
            self.assertEqual(canciones_2[0]["titulo"],"prueba2")
