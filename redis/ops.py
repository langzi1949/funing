# coding = utf-8

from redis import StrictRedis, ConnectionPool

pool = ConnectionPool(host="192.168.99.100", port=6379, db=0)
redis = StrictRedis(connection_pool=pool)

def main():
    #redis.set("name","Kobe")
    #print("-->"+redis.get("name").decode())
    redis.hset("lesson:feedback","1001",'{"lessonPlanId":"1001"}')

if __name__ == '__main__':
    main()