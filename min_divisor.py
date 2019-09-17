n=int(input("enter a number"))
lst=[]
for i in (2,n+1):
    if n%i==0:
        lst.append(i)
print(min(lst))        