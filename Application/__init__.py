import sqlite3
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from pymysql import *
from os import getenv
#from decouple import config

app = Flask(__name__)
#database = config('DATABASE_URI')

app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URI')
#app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///BookDB.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = getenv('SECRET_KEY', "powerful secretkey")
db = SQLAlchemy(app)

import Application.routes