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
    with open("D:\\desktop\\all_mobile.txt",encoding='utf-8') as open_file,open("D:\\desktop\\qyl_loan_mobile.txt",'a',encoding='utf-8') as w_file:
        for line in open_file:
            param = line.strip()
            sql_ykqj = 'select count(1) from base.t_cash_exec ex LEFT JOIN  base.t_cash_order co on ex.txn_id = co.txn_id \
                    LEFT JOIN base.t_cash_apply ca on co.apply_id=ca.apply_id where ca.mobile_no =%s and ex.od_day>=60'
            cursor.execute(sql_ykqj,(param))
            count_ykqj = cursor.fetchone()
            sql_qyl = "select  count(1) From  base.lo_loan_order a INNER JOIN base.lo_repay_plan_exe b \
                            on a.loan_order_id=b.loan_order_ref   \
                        where a.loan_status='01' and  b.is_enable='1' and  b.is_late='1' \
                        and a.mobile_no=%s and  a.business_code ='QYL' and b.status in('01','10','12','13','11') and b.late_days>=60"
            cursor.execute(sql_qyl,(param))
            count_qyl = cursor.fetchone()
            count +=1
            print('第'+str(count)+"次:"+str(count_ykqj[0])+"----"+str(count_qyl[0]))
            #拼接数据
            if int(count_ykqj[0])>0 or int(count_qyl[0])>0:
                sql_str_1 =param+"\n"
                w_file.write(sql_str_1)
            # if int(count_ykqj[0])==0 and int(count_qyl[0])>0:
            #     sql_str_2 ="update t_risk_blacklist set prod_code ='QYL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
            #     w_file.write(sql_str_2)
            # if int(count_ykqj[0])>0 and int(count_qyl[0])>0:
            #     sql_str_3 ="update t_risk_blacklist set prod_code ='ALL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
            #     w_file.write(sql_str_3)

    #提交
    conn.commit()
  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
if __name__ == '__main__':
    main()