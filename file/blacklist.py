# coding = utf-8
def main():
    #set
    set1 = set()
    set2 =set()
    set3 =set()
    set4 =set()
    with open('D:\\desktop\\整理的数据\\qyl_idno.txt',encoding='UTF-8') as o_f1,open('D:\\desktop\\整理的数据\\ykqj_idno.txt',encoding='UTF-8') as o_f2:
        for line in o_f1:
            if line is not None :
                set1.add(str(line.strip()))
        
        for line in o_f2:
            if line is not None:
                set2.add(str(line.strip()))
    
    print(len(set1))
    print(len(set2))
    with open('D:\\desktop\\整理的数据\\risk_idno.txt',encoding='UTF-8') as o_f3,open('D:\\desktop\\SQL\\update_idno.txt','a',encoding='UTF-8') as w_f:
        for line in o_f3:
            param = str(line.strip())
            #print(param)
            if param in set1 and param not in set2:
                # sql_str_1 ="update t_risk_blacklist set prod_code ='QYL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                sql_str_1 ="('QYL','IDCARD','"+param+"'),\n"
                w_f.write(sql_str_1)
            if param in set2 and param not in set1:
                # sql_str_1 ="update t_risk_blacklist set prod_code ='YKQJ' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                sql_str_1 ="('YKQJ','IDCARD','"+param+"'),\n"
                w_f.write(sql_str_1)



    with open('D:\\desktop\\黑名单用户\\钱有路身份证黑名单.txt',encoding='UTF-8') as o_f11,open('D:\\desktop\\黑名单用户\\一刻千金身份证黑名单.txt',encoding='UTF-8') as o_f21:
        for line in o_f11:
            if line is not None :
                set3.add(str(line.strip()))
        
        for line in o_f21:
            if line is not None:
                set4.add(str(line.strip()))
    
    print(len(set3))
    print(len(set4))
    with open('D:\\desktop\\黑名单用户\\all_idno.txt',encoding='UTF-8') as o_f31,open('D:\\desktop\\SQL\\update_idno.txt','a',encoding='UTF-8') as w_f1:
        for line in o_f31:
            param = str(line.strip())
            #print(param)
            if param in set3 and param not in set4:
                # sql_str_1 ="update t_risk_blacklist set prod_code ='QYL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                sql_str_1 ="('QYL','IDCARD','"+param+"'),\n"
                w_f1.write(sql_str_1)
            if param in set4 and param not in set3:
                # sql_str_1 ="update t_risk_blacklist set prod_code ='YKQJ' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                sql_str_1 ="('YKQJ','IDCARD','"+param+"'),\n"
                w_f1.write(sql_str_1)
            if param in set3 and param  in set4:
                # sql_str_1 ="update t_risk_blacklist set prod_code ='ALL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                sql_str_1 ="('ALL','IDCARD','"+param+"'),\n"
                w_f1.write(sql_str_1)
            if param not in set3 and param  not in set4: 
                # sql_str_1 ="update t_risk_blacklist set prod_code ='ALL' where bl_type='MOBILENO' and bl_no ='"+param+"';\n"
                sql_str_1 ="('ALL','IDCARD','"+param+"'),\n"
                w_f1.write(sql_str_1)
if __name__ == '__main__':
    main()