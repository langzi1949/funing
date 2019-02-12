if __name__ == '__main__':
	# 这是python中的列表，相当于java中的数组或者列表
	list =['open','close']
	print(list[0])
	list.insert(4, 'pudding')
	list.append('hebei')
	list.sort()
	print(list)
	# 进行倒序排序
	list.sort(reverse=True)
	print(list)
	# 使用sorted()进行临时排序
	books =['jiangsu','tianjin','beijing','shanghai']
	print(sorted(books))
	print(sorted(books,reverse=True))
	# 进行反转,注意这不是倒序
	books.reverse()
	print(books)