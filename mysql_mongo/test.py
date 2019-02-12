#coding = utf-8
import mongoTool as MongoTool

def main():
    collection = MongoTool.get_mongo_connect()['upay_info_logs']
    upay_list = collection.find({"_id":"1685617655729126303962308"})
    print(upay_list[0]['source_name'])

if __name__ == '__main__':
    main()