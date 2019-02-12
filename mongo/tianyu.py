# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types
import csv

'''
获取天御的信息
@param mobile_list 手机号码列表
'''
def get_sh_info(mobile_list,prodCode,page):
    uri = 'mongodb://gather:gather123@192.168.200.195:27017/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['tianyu_antifraud_log']
    json_list = collection.find({"mobileNo":{"$in":mobile_list},"prodCode":prodCode})
    arr_final =[]
    key_arr=['mobileNo','userName','idNo','riskScore','score','1','2','3','4','5','6','7','8','301','503','createTime']
    #计数
    count=1
    for line in json_list:
        dict_final = {}
        dict_final['mobileNo'] = line['mobileNo']
        dict_final['riskScore']=line['riskScore']
        dict_final['score']=line['score']
        dict_final['userName']=line['userName']
        dict_final['idNo']= line['idNo']
        dict_final['createTime'] = line['updateTime']
        if 'riskInfo' in line.keys():
            for riskinfo in line['riskInfo']:
                dict_final[str(riskinfo['riskCode'])]=str(riskinfo['riskCodeValue'])
        
        arr_final.append(dict_final)
        print("处理到第"+str(page)+"页,当前处理到:"+str(count)+"行")
        count += 1
        #print(dict_final)
    
    data = pd.read_json(json.dumps(arr_final))
    data_ri = data.reindex(columns=key_arr)
    data_ri.to_csv("D://desktop//tianyu_"+prodCode+".csv",encoding ='utf-8')

'''
读取文件取出手机号码
@param filename  文件名称
'''
def read_mobile_no(filename):
    mobile_set =set()
    #读取csv至字典
    csvFile = open(filename,'r',encoding='UTF-8')
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
    #获取天御数据
    for i in range(0,len(mobile_list),3000):
        get_sh_info(mobile_list[i:i+3000],'QYL',i/3000+1)
