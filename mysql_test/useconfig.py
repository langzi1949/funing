# conding = utf-8
import pymysql

def main():
    config = {
        'host':'192.168.200.214',
        'port':3306,
        'user':'namibank',
        'passwd':'namibank123',
        'db':'risk',
        'charset':'utf8'
    }
    conn = pymysql.connect(**config)
    # 创建游标
    cursor = conn.cursor()
    #执行
    effect_row = cursor.execute("select * from risk.t_risk_rule limit 10")
    print(effect_row)

if __name__ == '__main__':
    main()
