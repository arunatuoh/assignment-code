def interchange(list):
	first=list.pop(0)
	last=list.pop(-1)
	list.insert(0,last)
	list.append(first)
	return list
l=[24,25,26]
print(interchange(l))	