#Keyword Arguments
#page no:32


def func(a, b=5, c=10):
    
   print ('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)


#Default Arguments

def hello(wish,name='you'):
 return '{},{}'.format(wish,name)
print(hello("good morning"))

#Variable-length arguments

def txt(*names):
 for name in names:
    print("Hello",name)
txt("ELTON","WATSON","GOLD","CHRISTOPHER")


#Program to find area of a circle using function use 
  #single return value function with argument.

r=int(input("Enter the radius of the circle -- "))
pi=3.14
def areaofcircle(r):
    return pi*r*r
print (areaofcircle(r))



