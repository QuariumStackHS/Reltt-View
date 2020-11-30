from logging import exception
import warnings
from flask import config
from RELTT_WEB.logs import *
import datetime
from RELTT_WEB.plugins.apps.PL_apps import *

import os
from os import environ
HOST = environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
    PORT = 5555
def urlfor(strd):
    return f"http://{HOST}{PORT}/{strd}"

class pl_log:
    def __init__(self):
        self.type = ""
        self.str = ""
        self.gravity = 0
        self.when = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')
        


class pl_newlog(pl_log):
    def __init__(self, typed, strs, gravity,fromd):
        super().__init__()
        self.fromd=fromd
        self.type = typed
        self.str = strs
        self.gravity = gravity
        self.when = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')
class pl_view:
    def __init__(self,path,desc):
        self.path=path
        self.desc=desc
#import RELTT_Editor.plugins.plugtest as plt
Registerer=PL_Apps()
pluginlist=[]
pluginsconfig=[]
def load_plugins():
    pluginlist=[]
    pluginsconfig=[]
    for i in open("RELTT_WEB/plugins/pl.cfg","r").read().splitlines():
        try:
            global inp

            exec(f"from RELTT_WEB.plugins.{i} import *")
            exec(f"global j; j={i}_init(Registerer)")
            global j
            pluginsconfig.append(j)
            pluginlist.append(i)
        except Exception as e:
            newlogq=newlog(f"error {e}",f"loading plugin \"{i}\"",10)
            logger.Write(newlogq)
    return pluginlist, pluginsconfig
def reload_plugins():
    pluginlist=[]
    pluginsconfig=[]
    for i in open("RELTT_WEB/plugins/pl.cfg","r").read().splitlines():
        try:
            import importlib
            
            importlib.import_module("RELTT_WEB.plugins.{i}")
            exec(f"global j; j={i}_getconfig()")
            global j
            pluginsconfig.append(j)
            pluginlist.append(i)
        except Exception as e:
            newlogq=newlog(f"error {e}",f"loading plugin \"{i}\"",10)
            logger.Write(newlogq)
    return pluginlist, pluginsconfig

    