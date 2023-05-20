#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".


a = 33
b = 33
if a>b :
    print("a is greater than b")
elif a==b :
    print("a and b are equal")
else:
    print("a is greater than b")    

 #new  method of printing    
    
a = 2
b = 330

print("A") if a > b else print("B")



#AND(conditional operator)

a = 200
b = 33
c = 500

if a>b and b<c:
    print("both the conditions are true")
    
    
#Or
#The or keyword is a logical operator, and is used to combine conditional statements:

#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a<b or b<c:
    print("one of the conditions is true")
    
    
#Nested If
#You can have if statements inside if statements, this is called nested if statements.

x = 41
if x>20:
    print("x is above 20")
    if x>30:
        print("x is grater than 30")
        if x>40:
            print("x is grater than 40")
else:
    print("x is lesser than 30")        
    
    
