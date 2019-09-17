def ispelindrome(list_l):
	list_l = [121,123,989,575,1524,55]
	sum_ = 0
	for i in list_l:
		str_i = str(str_i)
		if ispelindrome(str_i):
        	sum_ = sum_ + i

print(sum_)        

