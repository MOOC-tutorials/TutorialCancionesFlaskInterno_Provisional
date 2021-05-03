
import os
from app import create_app, db
from vistas.vistas import *

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.create_all()

if __name__ == '__main__':
    app.run(debug = True)