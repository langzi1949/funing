# coding = utf-8
import requests
import json
from datetime import datetime 
import datetime
import types
import time


def post(startTime,endTime):
    url = "http://106.15.201.163:8121/df-creditPlatform/zhimatest/zhimaBackAllIn"
    #headers = {'content-type': 'application/json'}
    r = requests.post(url,data={'startTime':startTime,'endTime':endTime})
    return r.text



if __name__ == '__main__':
    #print(post('2017-11-14 08:00:00','2017-11-14 09:00:00'))
    # 创建时间
    beginTime = '2017-11-14 18:31:05'
    finalTime = '2017-11-14 19:12:00'
    #将字符串转为时间格式
    timeTuple = datetime.datetime.strptime(beginTime, '%Y-%m-%d %H:%M:%S')
    final_time_tuple = datetime.datetime.strptime(finalTime,'%Y-%m-%d %H:%M:%S')

    d= timeTuple
    delta = datetime.timedelta(seconds=30)
    count = 0
    while d<=final_time_tuple:
        startTime = str(d)
        #print(d)
        d +=delta
        endTime = str(d)
        print(startTime+"---"+endTime)
        #请求URL
        #post(startTime,endTime)
        time.sleep(2)
        #count +=1
        #print(count)

    #endTime = timeTuple + datetime.timedelta(seconds=1)
    #print(str(endTime))
