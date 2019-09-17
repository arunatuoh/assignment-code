str = input("enter multiple line of string:")
new_str = str.split()
d = {}
for i in new_str:
    if d.get(i):
        value = d.get(i)
        d[i] = value + 1
    else:
        d[i] = 1
print(d)