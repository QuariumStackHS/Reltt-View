from datetime import time
from logging import warning
import time
from RELTT_WEB.plugins.pluginloader import *
from RELTT_WEB.dbAPI import *
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from RELTT_WEB.plugins.apps.PL_apps import *
PLUGIN_NAME = "plugscript"
PLUGIN_VERSION = "0.0.1"
"""
folder in plugins
templates (will be copy to the main template dir)



"""

Registerer=None
plug=Plugin(PLUGIN_NAME,PLUGIN_VERSION)
global thiscfg
class plugscript(Plugin):
    def __init__(self,registerer:PL_Apps):
        self.Registerer=registerer
        self.Registerer.init(PLUGIN_NAME,PLUGIN_VERSION)
        self.aa=PL_App(self)
        self.aa.register_resource("plugins/Resource/")
        #Registerer.
@plug.add_route("")
def main_view():
    return render_template("plugscript/main.html")
# convention put PLuginname_Version
# this will prevent future probleme
@plug.route(f"/plugins/{PLUGIN_VERSION}/Logs")
def logspl():
    return "test"
