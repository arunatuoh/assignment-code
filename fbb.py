n = int(input("enter a number:"))
a = 0
b = 1
print(a)
print(b)
for i in range(1, n):
    if i % 2 == 0:
        c = a + b
        print(c)
        a = b
        b = c
    else:
        c = a + b
        a = b
        b = c
