# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types
import csv

def read_mongo(params,page):
    uri = 'mongodb://gather:gather123@192.168.200.195:27017/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['emd_info']
    emd_datas = collection.find({"PHONE":{'$in':params}})
    
    emd_list =[]
    #计数
    count =1
    print('========查询mongo结束=========')
    for data in emd_datas:
        emd_dict ={}
        emd_dict['PHONE']=data['PHONE']

        delay_data_money =''
        delay_data_plats = 0
        ###将数据转为json
        for result in data['RESULTS']:
            if result['TYPE'] == 'EMR012':
                for delay_data_info in result['DATA']:
                    # print(delay_data_info)
                    #取出其中的逾期的金额数据
                    # print(delay_data_info['MONEY'])
                    delay_data_money = delay_data_money+delay_data_info['MONEY']+'&&'
                    #取出其中的逾期平台数据
                    # print(delay_data_info['COUNTS'])
                    delay_data_plats = delay_data_plats+int(delay_data_info['COUNTS'])
        
        emd_dict['DELAY_MONEY'] = delay_data_money[:-2]
        emd_dict['DELAY_PLATFORM_COUNT'] = delay_data_plats

        emd_list.append(emd_dict)
        print("处理到第"+str(page)+"页,当前处理到:"+str(count)+"行")
        count += 1
    #print(emd_list)

    ##将数据存在pandas里面
    pandas_data = pd.read_json(json.dumps(emd_list))
    pandas_data_ri = pandas_data.reindex(columns={'PHONE','DELAY_MONEY','DELAY_PLATFORM_COUNT'})
    #输出到文件中
    pandas_data_ri.to_csv("D:\\desktop\\huadao_info.csv",encoding ='utf-8')
            

def main():
    mobile_set =set()
    #读取csv至字典
    csvFile = open('D:\\desktop\\QYL.csv','r')
    reader = csv.reader(csvFile)

    for item in reader:
        #忽略第一行
        if reader.line_num ==1:
            continue
        mobile_set.add(item[3].strip())
    
    csvFile.close()
    mobile_list = list(mobile_set)

    for i in range(0,len(mobile_list),3000):
        read_mongo(mobile_list[i:i+3000],i/3000+1)

if __name__ == '__main__':
    main()