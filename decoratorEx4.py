def my_decorator(some_function):
    def wrapper():
        
        num = 10

        if num == 10:
            print ("Yes!")
        else:
            print ("No!")
        
        some_function()
        print ("AFTER")

    return wrapper

def just_some_function():
    print ("Whee!!")

just_some_function = my_decorator(just_some_function)

just_some_function()
