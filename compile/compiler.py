import py_compile
import os
def h(cmd):
    os.system(cmd)


import shutil
import os

def copy_(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
h("cd ..")
copy_("RELTT_WEB/","build/RELTT_WEB/")

#os.chdir("d:\\tmp")
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
        if name.endswith(".py"):
           py_compile.compile(root+"/"+name,root+"/"+name+"c") 
           os.remove(root+"/"+name)
        print(os.path.join(root, name))
   for name in dirs:
        if name=="__pycache__":
           shutil.rmtree(root+"/"+name)
        print(os.path.join(root, name))

py_compile.compile("RELTT_WEB/views.py","build/RELTT_WEB/views.pyc" )

#py_compile.compile(file, cfile, dfile, doraise)