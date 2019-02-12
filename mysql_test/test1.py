# coding = utf-8
import pymysql


def main():
    #创建连接
    conn = pymysql.connect(host="192.168.200.214",port=3306,user='namibank', passwd='namibank123', db='risk', charset='utf8')

    # 创建游标
    cursor = conn.cursor()
    #执行
    effect_row = cursor.execute("select * from risk.t_risk_rule")
    row_1 = cursor.fetchone()
    print(row_1)
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
  
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

if __name__ == '__main__':
    main()
