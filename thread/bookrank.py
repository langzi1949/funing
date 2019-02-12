# encoding =utf-8
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen
import ssl

REGEX = compile(b'#([\d,]+) in Books')  #b代表的是byte
AMZN = 'http://amazon.com/dp/'
ISBNs= {'0132269937':'Core Python Programming','0132356139':'Pythnon Web Development with Django'}

def getRanking(isbn):
    context = ssl._create_unverified_context()
    page =uopen('%s%s' % (AMZN,isbn),context=context)
    data = page.read()
    page.close()
    return str(REGEX.findall(data)[0],'utf-8')

def _showRanking(isbn):
    print('- %r ranked %s' % (ISBNs[isbn],getRanking(isbn)))
    

def _main():
    print('At ',ctime(),'on Amazon-----')
    for isbn in ISBNs:
        #_showRanking(isbn)
        Thread(target=_showRanking,args=(isbn,)).start()

@register
def _atexit():
    print('all Done at ',ctime())

if __name__=='__main__':
    _main()