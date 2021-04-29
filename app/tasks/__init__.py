from celery import Celery


def make_celery():
   celery = Celery(__name__, broker='redis://localhost:6379/0', include=['vistas.vistas'])
   return celery

celery = make_celery()
