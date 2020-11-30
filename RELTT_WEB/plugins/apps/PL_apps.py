# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
# [Clang 6.0 (clang-600.0.57)]
# Embedded file name: ./build/RELTT_WEB/plugins/apps/PL_apps.py
# Compiled at: 2020-11-28 10:34:59
# Size of source mod 2**32: 573 bytes
import os
from RELTT_WEB.dbAPI import *
from flask import send_from_directory
from RELTT_WEB.logs import *
class Plugin:
    
    def __init__(self,name,version) -> None:
        self.routes=[]
        self.__name=name
        self.__version=version
        self.PLbaseURL=f"/{self.__name}/{self.__version}/"
    def add_route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.routes.append(endpoint)
            L=log(f"{self.__name} Instance")
            L.fromd=f"{self.__name} Instance"
            L.gravity=0
            L.type="Info"
            L.str=f"Rule for path: \"{self.PLbaseURL+rule}\" redirected to func: {f.__name__}"
            logger.logs.append(L)
            app.add_url_rule(self.PLbaseURL+rule, endpoint, f, **options)
            return f
        return decorator

class PL_Cards:

    def __init__(self, pathtothumbnail, name, desc, ct) -> None:
        self.Thumbnail = pathtothumbnail
        self.name = name
        self.desc = desc
        self.cardtype = ct


class PL_App:
    def register_resource(self,path):
        pythoncode=f"@app.route(\"{self.Plugin.PLbaseURL}<path:path>\")\n"
        pythoncode+=f'def __{self.Plugin.PLbaseURL.replace(".","").replace("/","")}(path):\n'
        pythoncode+=f'  return send_from_directory("{path}", path)'
        print()
        print(pythoncode)
        exec(pythoncode)
        
    def __init__(self,Pluginins:Plugin):
        self.cards = []
        self.Plugin=Pluginins
        self.name=""
    def addcard(self, card: PL_Cards):
        self.cards.append(card)


class PL_Apps:

    def __init__(self):
        self.__plugins=[]
        self._PL_Apps__apps = []
    def init(self,pluginname:str,pluginversion:str):
        self.__plugins.append(Plugin(pluginname,pluginversion))

    def addapp(self, application: PL_App):
        self._PL_Apps__apps.append(application)
    def __getapps(self):
        return self._PL_Apps__apps
# okay decompiling PL_apps.pyc
