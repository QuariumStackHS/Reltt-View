import threading
import random

class Thread():
    def __init__(self):
        self.msgs=[]
        pass
    def communicate(self,msg):
        self.msgs.append(msg)
    def get_comms(self):
        return self.msgs
    def del_comms(self):
        self.msgs.pop(0)
    def getoldestmsg(self):
        return self.msgs[0]
    def getMsgAndDel(self):
        rtnv=self.msgs[0]
        self.msgs.pop(0)
        return rtnv

class fThread:
    def __init__(self):
        self.desc = ""
        self.wishedoing = ""
        self.ID = None
        self.Thread = None
        self.INS=None
    def setIns(self,ins):
        self.INS=ins
    def getIns(self):
        return self.INS
    def setThread(self, Thread):
        self.Thread = Thread

    def setDesc(self, Desc):
        self.Desc = Desc

    def setWork(self, Work):
        self.wishedoing = Work

    def setID(self, ID):
        self.ID = ID

    def getThread(self):
        return self.Thread

    def getDesc(self):
        return self.Desc

    def getWork(self):
        return self.wishedoing

    def getID(self):
        return self.ID


class ThreadMNGR():
    def __init__(self):
        self.threads = []
        pass

    def CreateNewThread(self, funcins, args=("", 0)):
        newThread = threading.Thread(
            target=funcins, args=args if args != ("", 0) else None)
        newThread.start()
        StoredIns=fThread()
        StoredIns.setThread(newThread)
        self.threads.append(StoredIns)
        return StoredIns
    def countThreads(self):
        j=0
        for i in self.threads:
            if not i.getThread().isAlive():
                self.threads.remove(i)
            else:
                j+=1

        return j
