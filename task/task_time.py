# coding = utf-8

import sched
import time

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
scheduler = sched.scheduler(time.time,time.sleep)

# 周期性调度触发的函数
def print_time(inc):
    # to do something
    print(">>>> to do something")
    scheduler.enter(inc,0,print_time,(inc,))


# 默认参数为60s
def start(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    scheduler.enter(0, 0, print_time, (inc,))
    scheduler.run()


if __name__ == '__main__':
    start(5)


