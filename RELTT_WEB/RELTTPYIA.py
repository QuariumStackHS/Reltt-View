import os
import sys
import inspect



class project:
    def gencode(self):
        code=""
        for i in self.importse:
            code+=i+"\n"

        for i in self.funcs:
            code+=i+"\n"

        return code
    def addclass(self,classe:str,code:str):
        self.classses.setdefault(classe,code)

    def addfunc(self,funcname:str,code:str,classe=None):
        if classe!=None:
            self.classes[self.classses[classe]]



        self.funcs.setdefault(funcname,code)
    def __init__(self):

        self.classses={}
        self.importse=[]
        self.imports={}
        self.funcs={}
        self.currenttab="    "
        self.inteli=[]
        pass
    def importE(self,package:str):
        self.importse.append(f"import {package}")
        exec(f"global i; i=dir({package})")
        global i
        self.inteli.append(i)
        self.imports.setdefault(package,i)

