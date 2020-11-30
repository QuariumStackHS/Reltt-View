from datetime import time
from logging import warning
import time
from RELTT_WEB.plugins.pluginloader import *
from RELTT_WEB.dbAPI import *
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify

PLUGIN_NAME = "plugscript"
PLUGIN_VERSION = "0.0.1"
@app.route(f"/plugins/{plugin_name}")
def main_view():
    return render_template("plugscript/main.html")

Registerer=None
global thiscfg

def plugscript_getconfig(Registerer:PL_Apps):
    Registerer=Registerer
    Registerer.addapp

# convention put /plugins/{plugin_name}/view_name
# this will prevent future probleme
@app.route(f"/plugins/{plugin_name}/Logs")
def logspl():
    return "test"
