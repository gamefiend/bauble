from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app import * 
from models import *
from views import *
from forms import *

def startup():
    db.create_all()
    app.run()
