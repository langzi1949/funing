if __name__ == '__main__':
	dim = (200,40)
	print(dim[0])
	# 尝试修改元素的值
	# dim[0]=50  这样会报错, TypeError: 'tuple' object does not support item assignment
	for value in dim:
		print(value)
	# 元组不可以赋值,但是可以进行修改变量 以下的修改变量是没有问题的
	dim_1 = ('A','jiangsu')
	print(dim_1[0])
	dim_1 =('B','shanghai')
	print(dim_1[0])

	list =[]
	if list:
		print('list is not empty')
	else:
		print('list is empty')

	