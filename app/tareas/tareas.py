from celery import Celery
from app import create_app, db
from modelos.modelos import Album, Cancion, CancionSchema
import os
cancion_schema = CancionSchema()
import sqlalchemy


app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def registrar_cancion(id_album, cancion_json):
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        album = Album.query.get_or_404(id_album)
        nueva_cancion = Cancion(titulo=cancion_json["titulo"], minutos=cancion_json["minutos"], segundos=cancion_json["segundos"], interprete=cancion_json["interprete"])
        album.canciones.append(nueva_cancion)
        db.session.commit()
        return cancion_schema.dump(nueva_cancion)

