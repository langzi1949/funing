# encoding = utf-8
'''
创建Thread实体类 传给他一个可调用的类实例
'''
import threading
from time import sleep,ctime

loops =[4,2]

class ThreadFun(object):
    def __init__(self,func,args,name=''):
        self.name= name
        self.func = func
        self.args = args

    def __call__(self):
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
        t = threading.Thread(target=ThreadFun(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    
if __name__=='__main__':
    main()
    

