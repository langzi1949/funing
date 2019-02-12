# encoding = utf-8
'''
派生Thread的子类,并创建子类的实例
'''
import threading
from time import sleep,ctime

loops =[4,2]

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        #threading.Thread.__init__(self)
        #super(MyThread,self).__init__()
        super().__init__()
        self.name =name
        self.func = func
        self.args = args
    
    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print('start loop ',nloop,'--',ctime())
    sleep(nsec)
    print('loop ',nloop,'Done --',ctime())

def main():
    print('starting --',ctime())
    threads = []
    nloops =range(len(loops))

    #创建两个线程实例
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    
if __name__=='__main__':
    main()
    

