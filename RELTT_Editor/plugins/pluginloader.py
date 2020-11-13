from logging import exception
import warnings
from flask import config
from RELTT_Editor.logs import *

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

class pl_config:
    def __init__(self,plname,plv,pln,plmainp,desc,logopath,errors,warnings,logs):
        self.plugin_name=plname
        self.plugin_desc=desc
        self.plugin_logo=logopath
        self.plugin_version=plv
        self.notification=pln
        self.logs=logs
        self.mainpage=plmainp
        self.errors=errors
        self.warnings=warnings
        self.views=[]
    def add_view(self,path,desc=None):
        if type(path)==type(pl_view):
            self.views.append(path)
        else:
            av=pl_view(path,desc)
            self.views.append(av)

        pass
#import RELTT_Editor.plugins.plugtest as plt
pluginlist=[]
pluginsconfig=[]
def load_plugins():
    pluginlist=[]
    pluginsconfig=[]
    for i in open("RELTT_Editor/plugins/pl.cfg","r").read().splitlines():
        try:
            exec(f"from RELTT_Editor.plugins.{i} import *")
            exec(f"global j; j={i}_getconfig()")
            global j
            pluginsconfig.append(j)
            pluginlist.append(i)
        except Exception as e:
            newlogq=newlog(f"error {e}",f"loading plugin \"{i}\"",10)
            logger.Write(newlogq)
    return pluginlist, pluginsconfig
    