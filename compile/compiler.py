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
delpy=0
cachedpy=0
for root, dirs, files in os.walk("build/RELTT_WEB/", topdown = False):
   for name in files:
        if name.endswith(".py"):
            py_compile.compile(root+"/"+name,root+"/"+name+"c") 
            os.remove(root+"/"+name)
            #print(os.path.join(root, name))
   for name in dirs:
        if name=="__pycache__":
            for r,d,f in os.walk(os.path.join(root,name)):
                for i in f:
                    cachedpy+=1

            shutil.rmtree(root+"/"+name+"/")
            delpy+=1
            
print(f"{str(delpy)} Pycache(s) deleted\n{str(cachedpy)} python precompile have been recompile")
py_compile.compile("RELTT_WEB/views.py","build/RELTT_WEB/views.pyc" )
a=input("finishing compile runserver?")
if a=="y":
    h("cd build && python3 runserver.py")
#py_compile.compile(file, cfile, dfile, doraise)