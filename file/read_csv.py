# coding = utf-8
import csv

def main():
    #读取csv至字典
    csvFile = open('D:/desktop/name.csv','r')
    reader = csv.reader(csvFile)

    #建立空dict
    result = {}
    for item in reader:
        #忽略第一行
        if reader.line_num ==1:
            continue
        result[item[0]]=item[1]
    
    csvFile.close()
    print(result)
if __name__ == '__main__':
    main()