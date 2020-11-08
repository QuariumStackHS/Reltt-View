from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    passw = db.Column(db.String(100))
    maxdata=db.Column(db.Integer)
    
    def __init__(self, name, passw):
        self.name = name
        self.passw = passw
        self.maxdata=10 #everyone get 10 GB of storage