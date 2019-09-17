str=input("enter multiple line of string:")
new_str=""
for i in str:
    if i.isupper():
        new_str.add(i)
print(new_str)        