import re
s="""In this tutorial, you'll learn about Python file operations.
 More specifically, opening a file, reading from it, writing into 
 it, closing it, and various file methods that you should be aware
 of"""
s1=re.findall("fr.*m",s)
s2=re.findall("sh.+d",s)
s3=re.search("(.*) (this) (.*?) (.*) (.+?) (.*)",s)
s4=re.search("(?<=el)\w+","elton")
s5=re.split("this",s)
s6=re.sub("this","is",s)
s7=re.compile("[p-y-t]+[h-o-n]")
s8=s7.findall(s)
print(s8)