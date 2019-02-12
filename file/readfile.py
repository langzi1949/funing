#coding =utf-8
if __name__ == '__main__':
	# this is mac file path
	# with open('/Users/langzi/python/testfile') as file_obj:
	with open('D:/desktop/Untitled-1.py') as file_obj:
		contents = file_obj.read()
		print(contents.rstrip())  #用于删除字符串末尾的空白
		