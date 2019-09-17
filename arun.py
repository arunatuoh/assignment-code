n=int(input("enter a number:"))
factorial=1
if n==0:
    print("factorial og 0 is 1")
elif n<0:
    print("negative no does not have fdactorial")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)