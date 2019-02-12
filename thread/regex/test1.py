# encoding =utf-8
import re

# match 是从字符串的起始位置进行匹配
m = re.match('foo', 'football is my fav')
if m is not None:
    print(m.group())

# search 是从任意一个位置进行匹配的
s = re.search('bar', 'hellobarxx')
print(s.group())

# 匹配多个字符串
bt = 'bat|bit|bet'
m = re.search(bt,'bat')

#匹配任意个字符
anychar = '.j'
m = re.search(anychar,'jjava')
m.group()

#创建字符集
m = re.match('[cr][0-9]a[a-z]','r2ay')
print(m.group())

