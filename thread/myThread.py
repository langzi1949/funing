# encoding = utf-8
import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        super().__init__()
        self.func = func
        self.args = args
        self.name = name
    
    def getRest(self):
        return self.res
    
    def run(self):
        print('starting',self.name,'--',ctime())
        self.res = self.func(*self.args)
        print(self.name,' Done --',ctime())