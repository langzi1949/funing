# encoding = utf-8
'''
读取文件，将json转换为dict
'''
import json
import pandas as pd
'''
读取文件，将数据转换为json数据
'''


def read_file(filename):
    # 存放所有的key
    key_set = set()
    dict_list = []
    with open(filename, encoding='utf-8') as op_file:
        for line in op_file:
            dict_temp = {}
            if not line.strip():
                continue
            # 将数据字符串转为json数据
            a_list = json.loads(line.strip())
            for v in a_list:
                # 将这些key放入到set中
                key_set.add(str(v['name']))
                dict_temp[v['name']] = v['value']
            # 添加到dict_list
            dict_list.append(dict_temp)
    # 开始处理产生的所有数据
    # print(dict_list)
    execute_file(key_set, dict_list)


def execute_file(key_set, dict_list):
    data = pd.read_json(json.dumps(dict_list))
    data_ri = data.reindex(columns=list(key_set))
    data_ri.to_csv("D://desktop//text.csv", encoding='utf-8')


if __name__ == '__main__':
    read_file('D:\\desktop\\CMBC2.txt')
