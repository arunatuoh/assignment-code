num = int(input("enter a number:"))
if num>1:
    for i in range(2,num//2):
        if num % i == 0:
            print(num,"is not prime")
        else:
            print(num,"is prime")
            break
    else:
        print(num," is not prime")        