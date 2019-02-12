# coding = utf-8
import dbTool as DbTool

def main():
    # get connection
    conn = DbTool.get_prod_risk_conn()
    # 创建游标
    cursor = conn.cursor()
    #执行
    set1 =set()
    count =1
    #读取
    with open('D:\\desktop\\1.txt',encoding='UTF-8') as open_file:
        for line in open_file:
            value = line.strip()
            sql = 'select distinct bank_zh from risk.t_risk_bankcard where raid=%s'
            effect_row = cursor.execute(sql,(value))
            data = cursor.fetchone()
            set1.add(data[0])
            count +=1
            #print(count)
    # 提交，不然无法保存新建或者修改的数据
    #print(len(set))
 
    conn.commit()
  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    with open('D:\\desktop\\2.txt','w',encoding='UTF-8') as w_file:
        for v in set1:
            va = str(v)+'\n'
            print(va)
            w_file.write(va)


# def write_doc():
#     with open() as wf:

if __name__ == '__main__':
    main()