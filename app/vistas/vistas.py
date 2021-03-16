from flask import request
from modelos.modelos import db, Album, Medio, AlbumSchema
from flask_restful import Resource

album_schema = AlbumSchema()

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
