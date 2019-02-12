#coding= utf-8
import datetime
import time
import types

LONG_TIME='%Y-%m-%d %H:%M:%S'
SHORT_TIME='%Y%m%d%H%M%S'
LONG_DATE='%Y-%m-%d'
SHORT_DATE='%Y%m%d'
START_DAY_TIME='%Y-%m-%d 00:00:00'
END_DAY_TIME='%Y-%m-%d 23:59:59'


'''
时间戳，默认到毫秒
'''
def stamp(c_time,msec=True):
    #time.time() 获取的是秒级的时间戳
    if c_time is None:
        c_time = time.time()
    if msec is True:
        curr_t = int(c_time * 1000)
    else:
        curr_t = int(c_time)
    return curr_t


'''
格式化时间 2017-08-08 08:08:08
'''
def fmt_datetime(c_time):
    return fmt_d(c_time,LONG_TIME)


'''
按照时间戳进行格式化
'''
def fmt_d(c_time,fmt_str=None):
    if c_time is None:
        c_time = time.time()
    if fmt_str is None:
        fmt_str=LONG_TIME
    return time.strftime(fmt_str,time.localtime(c_time))



'''
将指定格式的字符串转换为时间戳,默认到毫秒
'''
def stamp_timestr(time_str,msec=True,fmt_str=None):
    if time_str is None or len(time_str) == 0:
        return None
    if fmt_str is None:
        fmt_str = LONG_TIME
    try:
        timeArray = time.strptime(time_str, fmt_str)
        timeStamp =''
        if msec is True:
            timeStamp = int(time.mktime(timeArray)) * 1000
        else:
            timeStamp = int(time.mktime(timeArray))
        return timeStamp
    except Exception as e:
        print(e)
    return None


'''
根据时间戳获得前一天的时间时间戳格式,默认是毫秒
'''
def yesterday_time(c_time,mesc= True):
    stamp(c_time,False)

    separate_stamp(c_time,mesc)


'''
根据时间戳换算相隔几天的时间戳,默认是毫秒
'''
def separate_stamp(c_time,mesc=True,days=None):
    if days is None:
        days = -1
    stamp(c_time,False)

    datetime_struct = datetime.datetime.fromtimestamp(c_time)
    separate_time  = datetime_struct + datetime.timedelta(days=days)

    return separate_stamp
    




def main():

if __name__ == '__main__':
    main()