from datetime import time
import time
from RELTT_Editor.plugins.pluginloader import *
from RELTT_Editor.dbAPI import *
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
                    plmainp=f"/plugins/{plugin_name}")


def plugscript_getconfig():
    return thiscfg

# convention put /plugins/{plugin_name}/view_name
# this will prevent future probleme
@app.route(f"/plugins/{plugin_name}/Logs")
def logspl():
    return "test"
