from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

#Creacion de la conexion con la base de datos postgres 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5433/db_test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.debug = True
conect = SQLAlchemy(app)



