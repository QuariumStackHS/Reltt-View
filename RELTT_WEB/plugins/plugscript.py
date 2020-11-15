from datetime import time
from logging import warning
import time
from RELTT_WEB.plugins.pluginloader import *
from RELTT_WEB.dbAPI import *
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify

plugin_name = "plugscript"
plugin_version = "0.0.1"
@app.route(f"/plugins/{plugin_name}")
def main_view():
    return render_template("plugscript/main.html")


global thiscfg
thiscfg = pl_config(plname=plugin_name,
                    plv=plugin_version,
                    pln=0,
                    plmainp=f"/plugins/{plugin_name}",
                    desc="this is the first Reltt plugin ever this is the test plugin that make all this project possible!",
                    logopath="/static/content/reltt.png",
                    logs=[pl_newlog("succese","loaded plugin successfuly",0,plugin_name)],
                    errors=0,
                    warnings=0)
def plugscript_getconfig():
    return thiscfg

# convention put /plugins/{plugin_name}/view_name
# this will prevent future probleme
@app.route(f"/plugins/{plugin_name}/Logs")
def logspl():
    return "test"
