from modelos.modelos import db, Cancion
from flask import Flask

app = Flask(__name__)
db.init_app(app)

with app.app_context():
    db.create_all()

    