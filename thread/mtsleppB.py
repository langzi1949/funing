# encoding = utf-8
import _thread
from time import sleep,ctime

loops =[4,2]

def loop(nloop,nsec,lock):
    print('start loop ',nloop,'--',ctime())
    sleep(nsec)
    print('loop ',nloop,' Done--',ctime())
    lock.release()

def main():
    print('starting --',ctime())
    locks = []
    nloops = range(len(loops))
    
    for i in nloops:
        lock = _thread.allocate_lock() # 获得锁对象
        lock.acquire() # 取得每个锁
        locks.append(lock)
    
    for  i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    
    for i in nloops:
        while locks[i].locked():
            pass

    print('all Done---',ctime())


if __name__ == '__main__':
    main()