# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types

'''
获取mongo中设备的LBS的信息
@param device_list
'''
def get_lbs_info(device_list):
    uri = 'mongodb://nbread:KohpsiSAHGQ2go6XFQbp@106.15.201.163:20000/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['gather_device_baseinfo']
    device_mongo_list = collection.find({"device_id":{"$in":device_list},"info_type":"LBS"})
    #json_list = collection.find({"phone":"2341234123"})
    
    key_arr=set()
    arr =[]
    for line in device_mongo_list:
        line.pop('_id')
        line.pop('id')
        line.pop('info_type')
        line.pop('gather_time')
        #转换数据
        line['create_time'] = line['create_time'].strftime("%Y-%m-%d %H:%M:%S")
        arr.append(line)
        for d,x in line.items():
            key_arr.add(d)
    
    data = pd.read_json(json.dumps(arr))
    data_ri = data.reindex(columns=list(key_arr))
    data_ri.to_csv("D://desktop//text2.csv",encoding ='utf-8')

'''
读取文件取出设备号
@param filename  文件名称
'''
def read_device_id(filename):
    device_list =set()
    with open(filename,encoding='utf-8') as op_file:
        for line in op_file:
            device_list.add(line.strip())
    
    return list(device_list)
             
if __name__ == '__main__':
    #获取设备id_list
    device_list = read_device_id("D:\\desktop\\YKQJ_BIZ_DEVICE.txt")
    #获取lbs信息
    get_lbs_info(device_list)
