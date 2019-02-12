# coding =utf-8
import dbTool as DbTool
'''
查询黑名单中的手机号码  2017-08-16 15:30:00 之前的数据
'''
def main():
    # get connection
    conn = DbTool.get_prod_risk_conn()
    # 创建游标
    cursor = conn.cursor()
    #计算数据
    count =0
    with open("D:\\desktop\\1.txt",encoding='utf-8') as open_file,open("D:\\desktop\\1_1.txt",'w',encoding='utf-8') as w_file:
        for line in open_file:
            param = line.strip()
            sql_ykqj = 'select count(1) from base.t_customer_ykqj where phone = %s'
            cursor.execute(sql_ykqj,(param))
            count_ykqj = cursor.fetchone()
            sql_qyl = 'select count(1) from base.t_customer_qyl where phone = %s'
            cursor.execute(sql_qyl,(param))
            count_qyl = cursor.fetchone()
            count +=1
            print('第'+str(count)+"次:"+str(count_ykqj[0])+'---'+str(count_qyl[0]))
            #拼接数据
            if int(count_ykqj[0])>0 and int(count_qyl[0])==0:
                sql_str_1 ="update t_risk_blacklist set prod_code ='YKQJ' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                w_file.write(sql_str_1)
            if int(count_ykqj[0])==0 and int(count_qyl[0])>0:
                sql_str_2 ="update t_risk_blacklist set prod_code ='QYL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                w_file.write(sql_str_2)
            if int(count_ykqj[0])>0 and int(count_qyl[0])>0:
                sql_str_3 ="update t_risk_blacklist set prod_code ='ALL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                w_file.write(sql_str_3)

    #提交
    conn.commit()
  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
if __name__ == '__main__':
    main()