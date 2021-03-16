from flask import request
from modelos.modelos import db, Album, Medio, AlbumSchema, Usuario, UsuarioSchema, Cancion, CancionSchema
from flask_restful import Resource

album_schema = AlbumSchema()
usuario_schema = UsuarioSchema()
cancion_schema = CancionSchema()

class VistaAlbums(Resource):

    def post(self):
        nuevo_album = Album(titulo=request.json["titulo"], anio=request.json["anio"], descripcion=request.json["descripcion"], medio=request.json["medio"])
        db.session.add(nuevo_album)
        db.session.commit()
        return album_schema.dump(nuevo_album)

    def get(self):
        return [album_schema.dump(al) for al in Album.query.all()]

class VistaAlbum(Resource):

    def get(self, id_album):
        return album_schema.dump(Album.query.get_or_404(id_album))

    def put(self, id_album):
        album = Album.query.get_or_404(id_album)
        album.titulo = request.json.get("titulo",album.titulo)
        album.anio = request.json.get("anio", album.anio)
        album.descripcion = request.json.get("descripcion", album.descripcion)
        album.medio = request.json.get("medio", album.medio)
        db.session.commit()
        return album_schema.dump(album)

    def delete(self, id_album):
        album = Album.query.get_or_404(id_album)
        db.session.delete(album)
        db.session.commit()
        return '',204


class VistaLogin(Resource):

    def post(self):
        nuevo_usuario = Usuario(nombre=request.json["nombre"], contrasena=request.json["contrasena"])
        db.session.add(nuevo_usuario)
        db.session.commit()

class VistaUsuario(Resource):

    def get(self, id_usuario):
        return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))

    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return '',204

    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        usuario.contrasena = request.json.get("contrasena",usuario.contrasena)
        db.session.commit()
        return usuario_schema.dump(usuario)

class VistaCanciones(Resource):

    def post(self):
        nueva_cancion = Cancion(titulo=request.json["titulo"], minutos=request.json["minutos"], segundos=request.json["segundos"], interprete=request.json["interprete"])
        db.session.add(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)
