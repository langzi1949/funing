# coding = utf-8

import schedule
import time

'''
定义一个工作的方法
'''
def job():
    print("I am  working.........")


# 每隔1分钟执行一次
schedule.every(1).minutes.do(job)
# 每隔1小时执行一次
#schedule.every().hour.do(job)
# 每天的10:30分执行
#schedule.every().day.at("10:30").do(job)
# 每周一的这个时候执行
#schedule.every().monday.do(job)
# 每周三的13:15分执行
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

