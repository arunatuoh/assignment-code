string=input("Enter the string:")
rev_string=string[:: -1]
print("reversed string:",rev_string)
if string == rev_string:
    print("string is palindrom")
else:
    print("string is not palindrom")   