def  myfun(name):
 print(name+"Elton")

myfun("email")
myfun("phone")
myfun("last name")
myfun("OTP")
myfun("age")



def myfun2(name,lastname):
 print(name+"  "+lastname)
myfun2("Elton","G") 



def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")




def my_functions(child3, child2, child1):
  print("The youngest child is " + child3)

my_functions(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




def my_function2(**kid):
  print("His last name is " + kid["lname"])

my_function2(fname = "Tobias", lname = "Refsnes")




def my_function3(country = "Norway"):
  print("I am from " + country)

my_function3("Sweden")
my_function3("India")
my_function3()
my_function3("Brazil")




def my_function4(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function4(fruits)



def my_function5(x):
  return 5 * x

print(my_function5(3))
print(my_function5(5))
print(my_function5(9))



# having an empty function definition like this, would raise an error without the pass statement
def myfunction6():
  pass



#Recursion
#Python also accepts function recursion, which means a defined function can call itself.


#Recursion Example

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

