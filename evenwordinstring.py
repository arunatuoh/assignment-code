def even_word_in_string(str):
str=str.split(" ")
for i in str:
    if len(i)%2==0:
        print(i)
str="my name is arun kumar singh" 
print(even_word_in_string)       