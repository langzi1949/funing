# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types

'''
获取mongo中设备的LBS的信息
@param user_id
'''
def get_lbs_info(user_ids):
    uri = 'mongodb://nbread:KohpsiSAHGQ2go6XFQbp@106.15.201.163:20000/gather'
    client = MongoClient(uri)
    db = client['gather']
    user_device_collection = db['gather_user_device']
    user_device_list = user_device_collection.find({"user_id":{"$in":user_ids}})
    
    key_arr=set()
    user_device_arr =[]
    device_ids = []
    for line in user_device_list:
        line.pop('_id')
        line.pop('create_time')
        user_device_arr.append(line)
        #将device_id暂存
        device_ids.append(line['device_id'])

    # 根据device_ids取出信息
    device_collection = db['gather_device_baseinfo']
    device_list = device_collection.find({"device_id":{"$in":device_ids},"info_type":"LBS"})

    final_arr =[]

    for line in device_list:

        line.pop('_id')
        line.pop('id')
        line.pop('gather_time')
        line.pop('info_type')
        #转换数据
        line['create_time'] = line['create_time'].strftime("%Y-%m-%d %H:%M:%S")
        #临时的字典
        temp_dict = line
        #进行封装
        for user_device in user_device_arr:
            if user_device['device_id'] == line['device_id']:
                temp_dict['user_id'] = user_device['user_id']+"_TEMP"
                #将数据放入到数据中
                final_arr.append(temp_dict)
    

    

    
    data = pd.read_json(json.dumps(final_arr))
    data_ri = data.reindex(columns={'user_id','device_id','info_data','create_time'})
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
    device_list = read_device_id("D:\\desktop\\YKQJ_USER.txt")
    #获取lbs信息
    get_lbs_info(device_list)
