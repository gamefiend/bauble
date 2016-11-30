import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_db = "db/bauble.db"
sqlite_url = "sqlite:///{}".format(os.path.join(basedir, sqlite_db)) 
print sqlite_url
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlite_url
db = SQLAlchemy(app)
