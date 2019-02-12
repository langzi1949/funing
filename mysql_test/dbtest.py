# coding = utf-8
import datetime
import os
#from mysqltest import dbTool as DbTool
import dbTool as DbTool
import json

def main():
    # get connection
    conn = DbTool.get_risk_conn()
    # 创建游标
    cursor = conn.cursor()
    #执行
    effect_row = cursor.execute("select * from risk.t_risk_district_quota_config")
    data = cursor.fetchall()
    #print(row_1)
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    #处理其中的data数据
    deal_data(data)
def deal_data(data):
    #print(data)
    dict_data = {}
    for row in data:
        if row[1]=='':
            dict_value ={}
            dict_value['code'] = row[5]
            dict_value['quota'] = str(row[4])
            dict_value['name'] = row[6]
            dict_value['parent_code'] = ''
            dict_data[row[5]] = dict_value
        else:
            dict_value = {}
            dict_value['code'] = row[1]
            dict_value['quota'] = str(row[4])
            dict_value['name'] = row[2]
            dict_value['parent_code'] = row[5]
            dict_data[row[1]] = dict_value
    
    ##写入文件中
    with open("D:\\desktop\\quota.txt",'w',encoding='utf-8') as w_file:
        json_data = json.dumps(dict_data,ensure_ascii=False)
        ##print(json_data)
        w_file.write(str(json_data))
if __name__ == '__main__':
    main()