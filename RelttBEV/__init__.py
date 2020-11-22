def Rimport(module:str):
    exec(f"import {module}");
    exec(f"global i; i=dir({module})");
    global i;
    return i;

print(Rimport("os"))