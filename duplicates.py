def duplicates(x):
	final_list=[]
	for i in range(len(x)):
    	if i not in final_list:
        	final_list.append(i)
    return final_list    	
x=[1,1,2,3,4,4,5,5]
print(duplicates(x))        
