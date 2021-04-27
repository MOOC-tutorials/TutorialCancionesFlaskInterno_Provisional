from modelos.modelos import db
from flask import Flask
from flask_restful import Api
from vistas.vistas import *
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

db.init_app(app)
api = Api(app)
jwt = JWTManager(app)



api.add_resource(VistaAlbums, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaUsuario, '/usuario/<int:id_usuario>')
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

