# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types
import csv

'''
获取新颜的信息
@param id_no_list 手机号码列表
'''
def get_sh_info(id_no_list,prod_code,page):
    uri = 'mongodb://gather:gather123@192.168.200.195:27017/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection1 = db['xinyan_radar_log']
    json_list1 = collection1.find({"idCard":{"$in":id_no_list},"productCode":prod_code})
    collection2 = db['xinyan_wash_log']
    json_list2 = collection2.find({"idCard":{"$in":id_no_list},"productCode":prod_code})

    json_arr =[]
    

    for line in json_list2:
        json_dict ={}
        json_dict['idCard'] = line['idCard']
        json_dict['washBlack_data'] = line['washBlack_data']
        json_dict['washWhite_data'] = line['washWhite_data']
        json_arr.append(json_dict)

    arr = []
    key_arr = set()
    count =1
    #合并集合的数据
    for line in json_list1:
        xinyan_dict = {}
        xinyan_dict['create_time'] = line['create_time']
        for k,v in line.items():
            #获取身份证号码
            if k =='idCard':
                xinyan_dict['id_card'] = str(v)
                #取洗白的数据
                for line1 in json_arr:
                    for k1,v1 in line1.items():
                        #判断数据是否存在id_card_list
                        if k1 == 'idCard' and v1 == v:
                            #直接取line的值
                            if line1['washBlack_data'] is not None:
                                xinyan_dict['wash_black.tag'] = line1['washBlack_data']['tag']
                                xinyan_dict['wash_black.tagDesc'] = line1['washBlack_data']['tagDesc']
                            if line1['washWhite_data'] is not None:
                                xinyan_dict['wash_white.tag'] = line1['washWhite_data']['tag']
                                xinyan_dict['wash_white.tagDesc'] = line1['washWhite_data']['tagDesc']
                            continue
            #获取三种雷达
            if k =='applyRadar_data' and v is not None:
                for k1,v1 in v.items():
                    xinyan_dict[k1] = v1
            if k =='behaviorRadar_data' and v is not None:
                for k1,v1 in v.items():
                    xinyan_dict[k1] = v1
            if k =='currentRadar_data' and v is not None:
                for k1,v1 in v.items():
                    xinyan_dict[k1] = v1
            
            for k,v in xinyan_dict.items():
                key_arr.add(k)
            
        arr.append(xinyan_dict)
        print("处理到第"+str(page)+"页,当前处理到:"+str(count)+"行")
        count += 1
                        
    
    data = pd.read_json(json.dumps(arr))
    data_ri = data.reindex(columns=list(key_arr))
    data_ri.to_csv("D://desktop//xianyan_"+prod_code+".csv",encoding ='utf-8')
    #data_ri.to_csv("D://desktop//text.csv",header=True,index_label=['phone','id_card','STAN_FRD_LEVEL'])
    #print(data_ri)

'''
读取文件取出身份证号码
@param filename  文件名称
'''
def read_id_no(filename):
    id_set =set()
    #读取csv至字典
    csvFile = open(filename,'r')
    reader = csv.reader(csvFile)

    for item in reader:
        #忽略第一行
        if reader.line_num ==1:
            continue
        id_set.add(item[2].strip())
    
    csvFile.close()
    return  list(id_set)


             
if __name__ == '__main__':
    #获取手机号码list
    idno_list = read_id_no("D:\\desktop\\QYL.csv")
    for i in range(0,len(idno_list),3000):
        get_sh_info(idno_list[i:i+3000],'QYL',i/3000+1)
