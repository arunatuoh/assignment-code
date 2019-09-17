str="AB1$23singh459$"
sum=0
for i in str:
	if 57 >= ord(i) >= 48:
		sum = sum + int(i)

print(sum)