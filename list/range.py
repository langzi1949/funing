if __name__=='__main__':
	for value in range(1,10):
		print(value)
	# 指定step
	for value in range(1,10,2):
		print(value)
	# 列表解析
	list = [value*2 for value  in range(1,10)]
	print(list)
	list.sort(reverse = True)
	print(list)