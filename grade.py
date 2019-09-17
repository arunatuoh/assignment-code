sub1=int(input("enter the marks of 1st sub:"))
sub2=int(input("enter the marks of 2nd sub:"))
sub3=int(input("enter the marks of 3rd sub:"))
sub4=int(input("enter the marks of 4rth sub:"))
sub5=int(input("enter the marks of 5th sub:"))
a_m=(sub1+sub2+sub3+sub4+sub5)/5
if a_m>90:
    print("grade=A")
elif 90>=a_m>80:
    print("grade=B")
elif 80>=a_m>70:  
    print("grade=C")
elif 70>=a_m>60:
    print("grade=D")
else:
    print("grade=E")              