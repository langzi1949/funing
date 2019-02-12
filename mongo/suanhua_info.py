# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types
import csv

'''
获取算话的信息
@param mobile_list 手机号码列表
'''
def get_sh_info(mobile_list,prodCode,page):
    uri = 'mongodb://gather:gather123@192.168.200.195:27017/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['suanhua_logs']
    json_list = collection.find({"phone":{"$in":mobile_list},"prod_no":prodCode})
    arr =[]
    key_arr=[]
    #计数
    count =1
    for line in json_list:
        dict_0 = line
        if 'DATA' not in line.keys():
            continue
        dict_1 = line['DATA']
        dict_0.pop('DATA')
        dict_data = dict(dict_0, **dict_1)
        ##做一些转换
        x = time.localtime(float(line['timestamp']/1000))
        dict_data['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S',x)
        dict_data.pop('_id')
        arr.append(dict_data)
        for d,x in dict_data.items():
            key_arr.append(d)
        print("处理到第"+str(page)+"页,当前处理到:"+str(count)+"行")
        count += 1
    
    # print(key_arr)
    ##重组arr
    temp_arr =['','','','','']
    for value in key_arr:
        if 'phone'==value:
            temp_arr[0] = value
        if 'id_card' ==value:
            temp_arr[1] = value
        if 'real_name' ==value:
            temp_arr[2] = value
        if 'prod_no' == value:
            temp_arr[3] = value
        if 'timestamp' == value:
            temp_arr[4] = value
    for value in key_arr:
        if value not in temp_arr:
            temp_arr.append(value)
    #print(temp_arr)
    data = pd.read_json(json.dumps(arr))
    data_ri = data.reindex(columns=temp_arr)
    data_ri.to_csv("D://desktop//suanhua_"+prodCode+".csv",encoding ='utf-8')
    #data_ri.to_csv("D://desktop//text.csv",header=True,index_label=['phone','id_card','STAN_FRD_LEVEL'])
    #print(data_ri)

'''
读取文件取出手机号码
@param filename  文件名称
'''
def read_mobile_no(filename):
    mobile_set =set()
    #读取csv至字典
    csvFile = open(filename,'r')
    reader = csv.reader(csvFile)

    for item in reader:
        #忽略第一行
        if reader.line_num ==1:
            continue
        mobile_set.add(item[3].strip())
    
    csvFile.close()
    
    return list(mobile_set)
             
if __name__ == '__main__':
    #获取手机号码list
    mobile_list = read_mobile_no("D:\\desktop\\QYL.csv")
    #获取算话数据
    for i in range(0,len(mobile_list),3000):
        get_sh_info(mobile_list[i:i+3000],'YKQJ',i/3000+1)