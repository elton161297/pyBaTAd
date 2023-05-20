#Iterator
#tuple can be iterratable
mytuple = ("apple", "banana", "cherry")
p=iter(mytuple)
print(next(p))
print(next(p))
print(next(p))

#String can be iterratable
mystr="Apple"
p1=iter(mystr)
print(next(p1))
print(next(p1))
print(next(p1))
print(next(p1))
print(next(p1))

#List Can Be Iterratable
mylist = ["apple", "banana", "cherry"]
p2=iter(mylist)
print(next(p2))
print(next(p2))
print(next(p2))

#Number cannot be Iterratable
#mynum=123
#p3=iter(mynum)
#print(next(p3))
#print(next(p3))
#print(next(p3))

#Set can be iterratable
myset = {"apple", "banana", "cherry"}
p4=iter(myset)
print(next(p4))
print(next(p4))
print(next(p4))

#Dict key only iteratable
mydict={1:"apple",2:"orange",3:"pine apple"}
p5=iter(mydict)
print(next(p5))
print(next(p5))
print(next(p5))

#































