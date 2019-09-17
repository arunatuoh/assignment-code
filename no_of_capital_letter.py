str=input("enter multiple line of string:")
count=0
for i in str:
    if i.isupper():
        count=count+1
print(count)        