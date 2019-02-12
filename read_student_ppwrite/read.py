# coding = utf-8
import requests
import os


def writeFile(createDate,ossFileName):
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    s = requests.session()
    s.keep_alive = False # 关闭多余连接
    url = "https://hf-learning-test.oss-cn-hangzhou.aliyuncs.com/ppwrite/"+createDate+"/"+ossFileName+".txt"
    # print(url)
    r = requests.get(url)
    fileDir = "E:/Desktop/ppwrite/"+createDate
    isExists = os.path.exists(fileDir)
    if not isExists:
        os.makedirs(fileDir)
    fileName = fileDir+"/"+ossFileName+".txt"
    with open(fileName,'a') as f:
        f.write(r.text)

def readFile():
    count = 0
    with open('E:/desktop/pp.txt') as file_obj:
        for line in file_obj:
            # print(contents.rstrip())
            line_info = line.rstrip()
            line_split = line_info.split('&&ZMG&&')
            writeFile(line_split[1],line_split[0])
            count = count +1
            print(count)

if __name__ == '__main__':
    readFile()