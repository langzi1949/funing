#coding:utf-8

import os
import platform
file_path = os.path.dirname(__file__)+"/"  #文件路径
import warnings
warnings.filterwarnings("ignore")
import jieba    #分词包
import numpy    #numpy计算包
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode 
import re
import pandas as pd  
import matplotlib.pyplot as plt
from urllib import request
from bs4 import BeautifulSoup as bs

import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud  ,ImageColorGenerator  #词云包
from scipy.misc import imread

#分析网页函数
def getNowPlayingMovie_list():   
    resp = request.urlopen('https://movie.douban.com/cinema/nowplaying/shanghai/')        
    html_data = resp.read().decode('utf-8')    
    soup = bs(html_data, 'html.parser')    
    nowplaying_movie = soup.find_all('div', id='nowplaying')        
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')    
    nowplaying_list = []    
    for item in nowplaying_movie_list:    
        nowplaying_dict = {}        
        nowplaying_dict['id'] = item['data-subject']       
        for tag_img_item in item.find_all('img'):            
            nowplaying_dict['name'] = tag_img_item['alt']            
            nowplaying_list.append(nowplaying_dict)    
    return nowplaying_list

#爬取评论函数
def getCommentsById(movieId, pageNum): 
    eachCommentList = []; 
    if pageNum>0: 
         start = (pageNum-1) * 20 
    else: 
        return False 
    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' +'?' +'start=' + str(start) + '&limit=20' 
    #print(requrl)
    resp = request.urlopen(requrl) 
    html_data = resp.read().decode('utf-8') 
    soup = bs(html_data, 'html.parser') 
    comment_div_lits = soup.find_all('div', class_='comment') 
    for item in comment_div_lits: 
        if item.find_all('p')[0].string is not None:     
            eachCommentList.append(item.find_all('p')[0].string)
    return eachCommentList

def main():
    #循环获取第一个电影的前10页评论
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    for i in range(1):    
        num = i + 1 
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'], num)
        commentList.append(commentList_temp)

    #将列表中的数据转换为字符串
    comments = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()

    #使用正则表达式去除标点符号
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    # 去除标签符号以后，变成了一个纯字符串
    cleaned_comments = ''.join(filterdata)

    #使用结巴分词进行中文分词
    segment = jieba.lcut(cleaned_comments)
    words_df=pd.DataFrame({'segment':segment})

    #去掉停用词
    stopwords=pd.read_csv(file_path+"stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
    words_df=words_df[~words_df.segment.isin(stopwords.stopword)] # 其中 ~是取反

    #统计词频
    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

    bg_pic = imread(file_path+'3.jpg')
    #用词云进行显示
    if 'Windows' in platform.system():
        wordcloud=WordCloud(mask=bg_pic,font_path="simhei.ttf",background_color="white",max_font_size=80)
    else:
        wordcloud=WordCloud(font_path="/Library/Fonts/Songti.ttc",background_color="white",max_font_size=80)
    
    word_frequence = {x[0]:x[1] for x in words_stat.head(100).values}

    wordcloud=wordcloud.fit_words(word_frequence) #参数为dict类型
    image_colors = ImageColorGenerator(bg_pic)
    
    #显示词云
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

#主函数
main()