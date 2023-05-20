#Python Lambda
#lambda arguments : expression
#The expression is executed and the result is returned:
    
x = lambda a : a + 10
print(x(5))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
       


