# encoding ='utf-8'
'''
https://bitbucket.org/wswp/code
'''
from urllib import request
from urllib import error


def download1(url):
    '''
    最简单的下载
    '''
    return request.urlopen(url).read()


def download2(url):
    '''
    捕获异常
    '''
    print('Downloading:', url)
    try:
        html = request.urlopen(url).read()
    except error.URLError as e:
        print('download2 has Exception', e.reason)
        html = None
    return html


def download3(url, num_retries=2):
    '''
    出现500x异常时，进行尝试操作
    '''
    print('Downloading:', url)
    try:
        html = request.urlopen(url).read()
    except error.URLError as e:
        print('download3 has exception', e.reason)
        html = None
        if num_retries > 2:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX
                html = download3(url, num_retries - 1)
    return html


def download4(url, user_agent='wswp', num_retries=2):
