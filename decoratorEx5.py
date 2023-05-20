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

if __name__ == "__main__":
    my_decorator()
