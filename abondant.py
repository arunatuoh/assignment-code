n = int(input("enter a number:"))
fact_sum = 0
for i  in range(1,n):
    if n % i == 0:
        fact_sum=fact_sum+i
        if(fact_sum>n):
            print(n,"is aboundant")
            break
else:
    print(n,"is not aboundant")	
