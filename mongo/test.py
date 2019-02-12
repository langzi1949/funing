# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types

def main():
    uri = 'mongodb://nbread:KohpsiSAHGQ2go6XFQbp@106.15.201.163:20000/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['suanhua_logs']
    json_list = collection.find({"timestamp":{'$gt':1502121600000,'$lt':1503158400000},"prod_no":"QYL"}).sort('timestamp').limit(10000)
    #json_list = collection.find({"phone":"2341234123"})
    arr =[]
    key_arr=[]
    for line in json_list:
        dict_0 = line
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
    data_ri.to_csv("D://desktop//text2.csv",encoding ='utf-8')
    #data_ri.to_csv("D://desktop//text.csv",header=True,index_label=['phone','id_card','STAN_FRD_LEVEL'])
    #print(data_ri)

if __name__ == '__main__':
    main()
    # print(time.time())
    # 1502121600000
    # 1501689600000
    # 1500888937
    # x= time.localtime(1500888937.654)
    # print(time.strftime('%Y-%m-%d %H:%M:%S',x))

    # a_time = '2017-08-20 00:00:00'
    # a_time_format = time.strptime(a_time,'%Y-%m-%d %H:%M:%S')
    # print(time.mktime(a_time_format))
