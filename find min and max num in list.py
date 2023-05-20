#Python program to find smallest number in a list
def small_num(num):
    a=min(num)
    b=max(num)
    print("Minimum number is %s\n"%(a) ,"Maximum number is %s"%(b))
small_num([1,2,3,-1,110])