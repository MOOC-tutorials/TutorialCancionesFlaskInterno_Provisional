from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app import db

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    puntajes = db.Column("Puntajes", db.ARRAY(db.Float))

class CancionSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = Cancion
         load_instance = True
