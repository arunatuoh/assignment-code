n=int(input("enter a number:"))
lst=[]
for i in (2,n+1):
    n=n//10
    lst.append(i)
print(len(lst))     