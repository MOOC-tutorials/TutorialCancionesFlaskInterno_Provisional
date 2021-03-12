from modelos.modelos import db, Usuario, Album, Medio, Cancion, albumes_canciones, CancionSchema, AlbumSchema, UsuarioSchema
from flask import Flask

app = Flask(__name__)
db.init_app(app)

cancion_schema = CancionSchema()
album_schema = AlbumSchema()
usuario_schema = UsuarioSchema()

with app.app_context():
    db.create_all()
