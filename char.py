sentence=input("enter a sentence:")
count=[]
list1=[',[,@,_,!,#,$,%,^,&,*,(,),<,>,?,/,\,|,},{,~,:,],']
for char in sentence:
    if char in list1:
        count.append(char)
print("no of consonant in sentence is ",count)      