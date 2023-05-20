from decoratorEx5 import my_decorator

#just_some_function1 = my_decorator(just_some_function)
@my_decorator
def just_some_function():
    print ("Wheee!")

just_some_function()
