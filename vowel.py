sentence=input("enter a sentence:")
string1=sentence.upper()
print(string1)
count=0
list1=["A","E","I","O","U"]
for char in string1:
	if char in list1:
		count=count+1
print("no of vowel in sentence is ",count)		