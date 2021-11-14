from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:project_admin@34.105.227.92:3306/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')

#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

import application.models
import application.forms
import application.routes