# coding = utf-8
from pymongo import MongoClient
import datetime
import time
import pandas as pd
import json
import types
import csv

'''
获取索伦的信息
@param id_no_list 手机号码列表
'''
def get_sh_info(id_no_list,prod_code,page):
    uri = 'mongodb://gather:gather123@192.168.200.195:27017/gather'
    client = MongoClient(uri)
    db = client['gather']
    collection = db['sauron_credit_logs']
    json_list = collection.find({"data.user_idcard":{"$in":id_no_list},"prodCode":prod_code})
    arr =[]
    key_arr=[]

    #计数
    count =1 
    for line in json_list:
        sauron_dict = arrange_dict(line['data'])
        arr.append(sauron_dict)
        print("处理到第"+str(page)+"页,当前处理到:"+str(count)+"行")
        count += 1
    
    data = pd.read_json(json.dumps(arr))
    data_ri = data.reindex(columns={'user_idcard','user_phone','user_name','last_appear_idcard','last_appear_phone','used_idcards_cnt','used_phones_cnt','sn_score','sn_order1_contacts_cnt','sn_order1_blacklist_contacts_cnt','sn_order2_blacklist_contacts_cnt','sn_order2_blacklist_routers_cnt','sn_order2_blacklist_routers_pct','idcard_in_blacklist','phone_in_blacklist','in_court_blacklist','in_p2p_blacklist','in_bank_blacklist','last_appear_idcard_in_blacklist','last_appear_phone_in_blacklist','online_installment_cnt','offline_installment_cnt','credit_card_repayment_cnt','payday_loan_cnt','online_cash_loan_cnt','offline_cash_loan_cnt','others_cnt','search_cnt','search_cnt_recent_7_days','search_cnt_recent_14_days','search_cnt_recent_30_days','search_cnt_recent_60_days','search_cnt_recent_90_days','search_cnt_recent_180_days','org_cnt','org_cnt_recent_7_days','org_cnt_recent_14_days','org_cnt_recent_30_days','org_cnt_recent_60_days','org_cnt_recent_90_days','org_cnt_recent_180_days'})
    data_ri.to_csv("D://desktop//sauron_"+prod_code+".csv",encoding ='utf-8')
    #data_ri.to_csv("D://desktop//text.csv",header=True,index_label=['phone','id_card','STAN_FRD_LEVEL'])
    #print(data_ri)

'''
读取文件取出身份证号码
@param filename  文件名称
'''
def read_id_no(filename):
    mobile_set =set()
    #读取csv至字典
    csvFile = open(filename,'r')
    reader = csv.reader(csvFile)

    for item in reader:
        #忽略第一行
        if reader.line_num ==1:
            continue
        mobile_set.add(item[2].strip())
    
    csvFile.close()
    
    return list(mobile_set)

'''
根据返回的dict处理数据
'''
def arrange_dict(item_dict):
    #先构造一个dict
    sauron_dict = {}
    #循环遍历item_dict的数据
    for k,v in item_dict.items():
        #获取身份证号码
        if k == 'user_idcard':
            sauron_dict['user_idcard'] = str(v)
        #获取手机号码
        if k == 'user_phone':
            sauron_dict['user_phone'] = str(v)
        #获取姓名
        if k == 'user_name':
            sauron_dict['user_name'] = str(v)
        #身份证最近出现时间
        #取出基本信息
        if k == 'user_basic' and v is not None:
            sauron_dict['last_appear_idcard'] = v['last_appear_idcard']
            sauron_dict['last_appear_phone'] = v['last_appear_phone']
            sauron_dict['used_idcards_cnt'] = v['used_idcards_cnt']
            sauron_dict['used_phones_cnt'] = v['used_phones_cnt']
        #获取risk信息
        if k == 'risk_social_network' and v is not None:
            sauron_dict['sn_score'] = v['sn_score']
            sauron_dict['sn_order1_contacts_cnt'] = v['sn_order1_contacts_cnt']
            sauron_dict['sn_order1_blacklist_contacts_cnt'] = v['sn_order1_blacklist_contacts_cnt']
            sauron_dict['sn_order2_blacklist_contacts_cnt'] = v['sn_order2_blacklist_contacts_cnt']
            sauron_dict['sn_order2_blacklist_routers_cnt'] = v['sn_order2_blacklist_routers_cnt']
            sauron_dict['sn_order2_blacklist_routers_pct'] = v['sn_order2_blacklist_routers_pct']
        if k == 'risk_blacklist' and v is not None:
            sauron_dict['idcard_in_blacklist'] = v['idcard_in_blacklist']
            sauron_dict['phone_in_blacklist'] = v['phone_in_blacklist']
            sauron_dict['in_court_blacklist'] = v['in_court_blacklist']
            sauron_dict['in_p2p_blacklist'] = v['in_p2p_blacklist']
            sauron_dict['in_bank_blacklist'] = v['in_bank_blacklist']
            sauron_dict['last_appear_idcard_in_blacklist'] = v['last_appear_idcard_in_blacklist']
            sauron_dict['last_appear_phone_in_blacklist'] = v['last_appear_phone_in_blacklist']
        
        if k == 'history_org' and v is not None:
            sauron_dict['online_installment_cnt'] = v['online_installment_cnt']
            sauron_dict['offline_installment_cnt'] = v['offline_installment_cnt']
            sauron_dict['credit_card_repayment_cnt'] = v['credit_card_repayment_cnt']
            sauron_dict['payday_loan_cnt'] = v['payday_loan_cnt']
            sauron_dict['online_cash_loan_cnt'] = v['online_cash_loan_cnt']
            sauron_dict['offline_cash_loan_cnt'] = v['offline_cash_loan_cnt']
            sauron_dict['others_cnt'] = v['others_cnt']
        if k =='history_search' and v is not None:
            for k1,v1 in v.items():
                sauron_dict[k1] = v1
        
    return sauron_dict


             
if __name__ == '__main__':
    #获取手机号码list
    idno_list = read_id_no("D:\\desktop\\QYL.csv")
    #获取索伦数据
    for i in range(0,len(idno_list),3000):
        get_sh_info(idno_list[i:i+3000],'QYL',i/3000+1)
