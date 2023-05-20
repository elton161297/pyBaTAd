class Parent:
    def myMethod(self):
        print ("Calling Parent method")

class Child:
    def myMethod(self):
        print ("Calling Child method")

c = Child()

c.myMethod()
