def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y 

print("chose operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")
chose=input("enter a operation:")
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
if chose=="1":
	print(a+b)
elif chose=="2":
	print(a-b)
elif chose=="3":
	print(a*b)
elif chose=="4":
	print(a/b)
else:
	print("invaid chose")		

