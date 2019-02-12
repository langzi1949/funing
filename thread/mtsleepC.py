# encoding = utf-8
'''
创建Thread实体类 传给他一个函数
'''
import threading
from time import sleep,ctime

loops =[4,2]

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
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops:
        threads[i].join()
    
if __name__=='__main__':
    main()
    

