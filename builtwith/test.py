# encoding =utf-8
from urllib import request
from urllib import error
import re

def download(url,user_agent='wswp',num_retries=2):
    '''
    下载所需要爬虫的网页HTML
    '''
    print('进行网页的爬虫操作:',url)
    #创建一个头
    headers = {'User-Agent':user_agent}
    url_req= request.Request(url,headers=headers)
    try:
        html = request.urlopen(url_req).read().decode('utf-8')
    except error.URLError as e:
        print('访问',url,'出现异常:',e.reason)
        html = None
        if num_retries>0:
            if hasattr(e,'code') and 500<=e.code<600:
                #如果是5xx错误的话，进行重试机制
                return download(url,user_agent,num_retries-1)
    return html

def crawl_sitemap(url):
    # download  the sitemap file
    sitemap = download(url)
    # extract 抽取 链接
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html = download(link)
        print(html)
if __name__=='__main__':
    print(download('http://www.baidu.com'))
    #print(download('http://httpstat.us/500')) #测试5xx错误
    #crawl_sitemap('http://example.webscraping.com/sitemap.xml')
