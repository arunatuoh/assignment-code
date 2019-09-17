import cmath
a=floor(input("enter a:"))
b=floor(input("enter b:"))
c=floor(input("enter c:"))
d=((b**2)-(04*a*c))
s1=(-b-cmath.sqrt(d))/2*a
s2=(-b+cmath.sqrt(d))/2*a
print("no of solution:",(s1,s2))