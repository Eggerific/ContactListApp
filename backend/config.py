from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # protects from a hit from different url

app = Flask(__name__) # initialize flask application
CORS(app) # disable error

# storing file database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # create database instance