num=int(input("enter the number of coloumn:"))
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()    