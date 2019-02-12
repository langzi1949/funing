# coding = utf-8
import requests
import json

def read(filename):
    with open(filename,encoding='utf-8') as op_file:
        for line in op_file:
            get(line.rstrip())

def get(openid):

    url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=11__U80OG7E49T4_IQjP15GLP4R_-Tui8CBSRQA2GvSf30jt-y_XrwEWPrr4G2XNsmq_2njjwx98XtRxIpAoIrDTSLfhoPpC0XM4m7RvchLpa1rLx1HbUBBQNegVOH95U6tg70pjCe9fIeTbtCOPLNaABAHDF&openid="+openid+"&lang=zh_CN"
    r = requests.get(url)
    #print(json.loads(r.text))
    if('nickname' in json.loads(r.text).keys()):
        write('/Users/langzi/Desktop/nickname.txt',json.loads(r.text))

def write(filename,nickname):
    with open(filename,'a') as f:
       f.write(str(nickname))


if __name__ == '__main__':
    get("oQbfD1JNgKpO1bI2g01jXMdrcjFE")
    #read('/Users/langzi/Desktop/openid.txt')