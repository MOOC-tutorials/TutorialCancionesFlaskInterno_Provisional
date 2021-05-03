from celery import Celery
from app import create_app, db
from modelos.modelos import Album, Cancion, CancionSchema
import os
from celery.signals import task_postrun
from flask.globals import current_app
cancion_schema = CancionSchema()
import sqlalchemy



app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def registrar_cancion(id_album, cancion_json):
    album = Album.query.get_or_404(id_album)
    nueva_cancion = Cancion(titulo=cancion_json["titulo"], minutos=cancion_json["minutos"], segundos=cancion_json["segundos"], interprete=cancion_json["interprete"])
    album.canciones.append(nueva_cancion)
    db.session.commit()
    return cancion_schema.dump(nueva_cancion)

@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()
