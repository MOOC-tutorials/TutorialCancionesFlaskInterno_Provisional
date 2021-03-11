from modelos.modelos import db, Usuario, Album, Medio, Cancion, albumes_canciones
from flask import Flask

app = Flask(__name__)
db.init_app(app)

with app.app_context():
    db.create_all()
    