def anagram(str1,str2):
    if len(str1)!=len(str2):
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            return 0
    return 1

str1="arun"
str2="nura"
if anagram(str1,str2):
    print("string is anagram")
else:
    print("string is not anagram")