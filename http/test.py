# coding = utf-8
import requests
import json

def read():
    count = 0
    with open('D:\\desktop\\ccid.txt',encoding='utf-8') as open_file:
        for line in open_file:
            ## 拼装json数据
            data = {}
            data['prodCode'] ='QYL'
            data['userId'] = str(line.strip())
            data['overdueDegree'] = 'm1'
            data['isPayOff'] = '1'
            data['overdueDays'] = 1
            #print(json.dumps(data))
            count += 1
            print(count)
            ##访问http接口
            result = post(json.dumps(data))
            if 'SUCCESS' != result:
                print('出现异常。。。。。。'+str(line.strip()))
                break


def post(json_data):
    #url = "http://106.15.201.163:81/risk-auditing-service/risk/overdue/dealOverdue"
    url = "http://proxy.namifunds.com:8105/risk-auditing-service/risk/overdue/dealOverdue"
    
    headers = {'content-type': 'application/json'}
    r = requests.post(url,data=json_data,headers=headers)
    return r.text



if __name__ == '__main__':
    #main()
    read()