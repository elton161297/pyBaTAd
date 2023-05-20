#find the num invalid or not(1-10)
#num=int(input("Enter The Number Range from 1-10 - "))
def num1(num):
    for x in range(11):
        if num==x:
            print("Number Valid")
        else:
            print("Not Valid")
num1(int(input("Enter The Number Range from 1-10 - ")))