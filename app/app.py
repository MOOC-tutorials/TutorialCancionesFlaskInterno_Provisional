from modelos.modelos import db, Cancion
from flask import Flask

app = Flask(__name__)
db.init_app(app)

with app.app_context():
    db.create_all()
    c = Cancion(titulo="Prueba", minutos=2, segundos=20, interprete="Fulanito")
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

    