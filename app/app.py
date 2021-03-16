from modelos.modelos import db
from flask import Flask
from flask_restful import Api
from vistas.vistas import *

app = Flask(__name__)
db.init_app(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

api.add_resource(VistaAlbums, '/albumes')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

