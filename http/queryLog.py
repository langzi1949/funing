# coding = utf-8
import requests


def main():
    url = "http://d-nfs.hfjy.com/logs/xue/java/jetty/study/xue.gateway.learn/B/learn.log"
    r = requests.get(url)
    # 将数据存储到文件中
    writeLog(r.text)

def writeLog(logText):
    fileName = "e:\\Desktop\\learn.log"
    with open(fileName,'w',encoding ='utf-8') as f:
        f.write(str(logText))


if __name__ == '__main__':
    main()