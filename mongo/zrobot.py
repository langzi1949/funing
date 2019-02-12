# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types
import csv

'''
获取Zrobot的信息
@param mobile_list 手机号码列表
'''
def get_sh_info(mobile_list,prodCode,page):
    uri = 'mongodb://gather:gather123@192.168.200.195:27017/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['zrobt_credit_log']
    json_list = collection.find({"mobileNo":{"$in":mobile_list},"prodCode":prodCode})
    arr_final =[]
    key_arr=['mobileNo','userName','idNo','bankCardNo','score','field','target_lev','is_targeted',\
        'debt_lender_num_12m','loan_lender_num_1m','overdue_status_1m','overdue_status_3m','credit_card_num','loan_lender_num_6m',\
        'loan_sum_6m','loan_lender_num_3m','overdue_status_12m','overdue_status_6m',\
        'payment_sum_12m','loan_sum_1m','loan_sum_3m','loan_sum_12m','debt_lender_num_6m',\
        'loan_lender_num_12m','payment_sum_1m','debt_lender_num_3m','payment_sum_3m','payment_sum_6m','debit_card_num','debt_lender_num_1m','createTime']
    #计数
    count=1
    for line in json_list:
        dict_final = {}
        dict_final['mobileNo'] = line['mobileNo']
        dict_final['userName']=line['userName']
        dict_final['bankCardNo']=line['bankCardNo']
        dict_final['idNo']= line['idNo']
        dict_final['createTime'] = line['create_time']
        #判断有没有scoreData key
        if 'scoreData' in line.keys() :
            for d,x in line['scoreData'].items(): 
                dict_final[d] = x

        #判断有没有blackListData
        if 'blackListData' in line.keys():
            for d,x in line['blackListData'].items(): 
                dict_final[d] = x
        #判断行为标签
        if 'behaviorData' in line.keys():
            for d,x in line['behaviorData'].items(): 
                dict_final[d] = x
        
        arr_final.append(dict_final)
        print("处理到第"+str(page)+"页,当前处理到:"+str(count)+"行")
        count += 1
        #print(dict_final)
    
    data = pd.read_json(json.dumps(arr_final))
    data_ri = data.reindex(columns=key_arr)
    data_ri.to_csv("D://desktop//zrobot_"+prodCode+".csv",encoding ='utf-8',mode='a',index=False)

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
    #获取Zrobot数据
    for i in range(0,len(mobile_list),3000):
        get_sh_info(mobile_list[i:i+3000],'QYL',i/3000+1)