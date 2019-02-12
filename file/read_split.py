# coding = utf-8
import string
def readFile():
    count =5500 
    # 先读取文件
    with open("D:\\desktop\\address.txt",encoding='utf-8') as op_file,open("D:\\desktop\\new_czh_1.sql",'a',encoding='utf-8') as w_file:
        for line in op_file:
            # 打印出数据
            #print(line.rstrip())
            # 进行分割
            str1 = line.rstrip()
            arr = str1.split('|')
            # 进行数据的拼装
            count = count+1   
            sql = "('"+str(count)+"','"+arr[0]+"','"+arr[1]+"','"\
            +arr[2]+"','"+arr[3]+"','"+arr[4]+"','Y','system',SYSDATE(),SYSDATE()),\n"
            # print(sql)
            # 将这些数据进行写入文件
            w_file.write(sql)
if __name__ == '__main__':
    readFile()