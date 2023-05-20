#calling def function 1
#page 29
def sample():
    print("sample output 1")
    print("sample output 2")
    print("sample output 3")


sample()   
sample() 
sample()  

#calling def function 2

def div(a,b):
    c=a+b
    d=a-b
    print(c)
div(5,20)
div(3,7)

##calling def function 3

def dive(e,f):
    g=e+f
    h=e-f
    return g,h
j=dive(20,5)
print(j)