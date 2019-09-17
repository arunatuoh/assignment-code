def fib(n):
    a = 1
    b = 2
    sum = 2
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
        if (sum <= 4000000):
            if c % 2 == 0:
                sum = sum + c
       
    return sum


print(fib(4898))
