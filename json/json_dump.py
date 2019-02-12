# encoding = utf-8
'''
学习json的dump
'''
import json


def dump_json():
    '''
    json.dump方法
    '''
    numbers = [0, 1, 5, 6, 7, 3]
    filename = '/Users/langzi/Desktop/xx.txt'
    with open(filename, 'w') as file_obj:
        json.dump(numbers, file_obj)
    with open(filename) as file_w:
        print(json.load(file_w))


if __name__ == '__main__':
    dump_json()
