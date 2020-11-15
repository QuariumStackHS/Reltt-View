"""
Routes and views for the flask application.
"""
import os
import hashlib
import sys
import datetime
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
from time import sleep
from flask import copy_current_request_context
import threading
import datetime
from flask import Flask, redirect, url_for, render_template, request, session, flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from RELTT_WEB.dbAPI import users,db,app
from RELTT_WEB.logs import *
from RELTT_WEB.Drive import *
pathtohome="RELTT_Editor/homes/"

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///DB.RLT.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.secret_key = "EnterYoutSecretKey"

import RELTT_WEB.plugins.pluginloader as pld
plulist,plugcfg =pld.load_plugins()
@app.route('/profile')
def profile():
    return ""
def userlogged(session):
    if "user" in session and "passw" in session:
        return True
    else:
        return False
@app.route('/')
@app.route('/home')
def home():
    if "user" in session and "passw" in session:
        return render_template(
            'index.html',
            title='Home Page',
            year=datetime.datetime.now().year,
            logged=True
        )
    else:
        return render_template(
            'index.html',
            title='Home Page',
            year=datetime.datetime.now().year,
            logged=False
        )

@app.route('/logoff')
def logoff():
    if "user" in session:
        if "passw" in session:
            user = session["user"]
            passw = session["passw"]
            if passw != "":
                if user != "":
                    session.pop("user", None)
                    session.pop("passw", None)
                    flash("you log out", "info")
                    return redirect(url_for("home"))
                else:
                    return redirect(url_for("home"))
            else:
                return redirect(url_for("home"))
        else:
            return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route('/plugins')
def plugins():
    print(plugcfg[0].plugin_name)
    return render_template("plugins.html",pllst=plugcfg,logged=userlogged(session))
@app.route('/logs')
def logs():
    logs=logger.logs
    for i in plugcfg:
        for j in i.logs:
            logs.append(j)
    
    return render_template("logs.html",pllst=logs)

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.datetime.now().year,
        message='Your application description page.',
        logged=userlogged(session)
    )
@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=="POST":
        user=request.form["UN"]
        passw=request.form["PS"]
        if user!=passw:
            fu=users.query.filter_by(name=user).first()
            if fu:
                return render_template('register.html',title='register',        year=datetime.datetime.now().year,
                message=f'username: "{user}" is not available',logged=userlogged(session))
            else:

                nutc=users(user,hashlib.sha224(passw.encode()).hexdigest())
                db.session.add(nutc)
                db.session.commit()
                session["user"]=user
                session["passw"]=hashlib.sha224(passw.encode()).hexdigest()
                
                return redirect(url_for("home"))
            
        pass
    else:
        return render_template('register.html',title='register',        year=datetime.datetime.now().year,
        message='Your application description page.',logged=userlogged(session))
@app.route("/bg",methods=["POST","GET"])
def bg():
    if request.method=="GET":
        request.get
    return "tu aime les penis?"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["UN"]
        passw = request.form["PS"]
        if passw != "":
            if user != "":
                fu=users.query.filter_by(name=user,passw=hashlib.sha224(passw.encode()).hexdigest()).first()
                if fu:
                    session["user"]=fu.name
                    session["passw"]=fu.passw
                else:
                    flash("invalid information or your account is not set-up correcly", "info")
                    return render_template('login.html',title='login',        year=datetime.datetime.now().year,
                    message='You are not already register? go into the register page',logged=userlogged(session))

        return redirect(url_for("home"))
    else:
        return render_template('login.html',logged=userlogged(session))
@app.route("/Drive")
def drive():
    return ""
    
    


@app.route("/IDE")
def IDE():
    return render_template("IDE.html",title='Reltt-IDE',        year=datetime.datetime.now().year,
                    message='Reltt')



