sentence=input("enter a sentence:")
string1=sentence.upper()
print(string1)
count=0
list1=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z",]
for char in string1:
    if char in list1:
        count=count+1
print("no of consonant in sentence is ",count)      