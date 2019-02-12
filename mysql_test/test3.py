# coding = utf-8
import pymysql
import sys


def main():
    host = ""
    password = ""
    dbName = ""
    userName = 'hls'
    #创建连接
    conn = pymysql.connect(host=host,port=3306,user=userName, passwd=password, db=dbName, charset='utf8')

    # 创建游标
    cursor = conn.cursor()
    # 读取文件
    contents = ""
    with open('E:/Desktop/No1.txt') as file_obj:
        contents = file_obj.read()
        
    print(sys.getsizeof(contents))
    #执行
    #insert_row = cursor.execute("update lesson_plan_score set student_impove_suggestion =' "+contents+"' where id=32")
    #print(row_1)
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

if __name__ == '__main__':
    main()
