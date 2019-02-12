# coding = utf-8
import string
def readFile():
    count =1 
    # 先读取文件
    with open("D:\\desktop\\QYL1.txt",encoding='utf-8') as op_file,open("D:\\desktop\\new_czh_2.sql",'a',encoding='utf-8') as w_file:
        for line in op_file:
            # 打印出数据
            #print(line.rstrip())
            # 进行分割
            str1 = line.rstrip()
            arr = str1.split('\t')
            # 进行数据的拼装
            count = count+1   
            sql = "insert into t_risk_encryption_blacklist values('"+str(count)+"','MD5','QYL','"+arr[0]+"','"+arr[1]+"',MD5('"\
            +arr[0]+arr[1]+"'),NULL,NULL,SYSDATE(),SYSDATE());\n"
            # print(sql)
            # 将这些数据进行写入文件
            w_file.write(sql)
if __name__ == '__main__':
    readFile()