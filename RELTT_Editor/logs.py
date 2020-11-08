import datetime

def unreasolve():
    return "404 Page not found!"


logfile = f"logs/{datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')}"


class log:
    def __init__(self):
        self.type = ""
        self.str = ""
        self.gravity = 0
        self.when = datetime.datetime.now().strftime('%b-%d-%I%M%p-%G')


class newlog(log):
    def __init__(self, typed, strs, gravity):
        super().__init__()

        self.type = typed
        self.str = strs
        self.gravity = gravity


class logg:
    def __init__(self):
        self.logs = []

    def Write(self, logb: log):
        print(logb.when, logb.type,logb.str,logb.gravity)
        self.logs.append(logb)

    def remove(self, what):
        if type(what) == type(0):
            self.logs[what] = ""
        elif type(what) == type(log):
            self.logs.remove(what)

    def save(self):
        f = open(logfile, "a")
        f.write(f"""----{logfile}----\n""")
        for i in self.logs:
            f.write(f"{str(i.typed)} {str(i.gravity)}\t{str(i.when)}\t{str(i.str)}")
        f.close()


logger = logg()


