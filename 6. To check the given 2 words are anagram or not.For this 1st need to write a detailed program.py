# To check the given 2 words are anagram or not.For this 1st need to write a detailed program


def anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        print("Both are anagram")
    else:
        print("Not anagram")

str1="dog"
str2="god"
anagram(str1,str2)
