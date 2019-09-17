def remove_dup(l):
	temp = []
	for i in l:
		if i not in temp:
			temp.append(i)

	print(temp)


remove_dup([1,2,5,4,3,6,5,2,1,4,5,2,3,6,2,1,5,4])