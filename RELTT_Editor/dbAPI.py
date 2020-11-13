from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
"""
every project will start with this code:
BEF
{{preinit}}
import sys

def main(argc,argv):
    ...

if __name__=="__main__":
    main(len(sys.argv),sys.argv)
    {{postinit}}
EOF

we need to cover defs
classes
for-while
imports
preinit of python script (before the main func)


"""
class defs(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    projectname=db.Column(db.String(100))
    
    pyfile=db.Column(db.String(100))
    pyclass=db.Column(db.String(100)) 
    pycode= db.Column(db.String(10000))
    def __init__(self,projectname,pyfile,pyclass,pycode) -> None:
        self.projectname=projectname
        self.pyfile=pyfile
        self.pyclass=pyclass
        self.pycode=pycode

class projects(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    devs= db.Column(db.String(100))
    projectname=db.Column(db.String(100))
    def __init__(self, name, devs):
        self.projectname = name
        self.devs = devs

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    passw = db.Column(db.String(100))
    maxdata=db.Column(db.Integer)

    def __init__(self, name, passw):
        self.name = name
        self.passw = passw
        self.maxdata=10 #everyone get 10 GB of storage