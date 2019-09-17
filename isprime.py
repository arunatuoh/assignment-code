n=int(input("enter a number:"))
if n>1:
	for i in range(2,n):
		print("hello there")
		if n % i == 0:
			print("not prime number") 
	    else:
			print("is prime number")    
