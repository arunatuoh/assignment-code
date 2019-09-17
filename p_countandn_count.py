l=[1,-12,-2,1,-4,32,-45,4]
p_count=0
n_count=0
for i in l:
    if i>=0:
        p_count=p_count+1
    else:
        n_count=n_count+1
print(p_count)
print(n_count)            