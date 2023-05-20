# Implement Python Script to check given number is Armstrong or not.
amg=list(input("Enter The Number  - "))
for x in amg:
    num=x*x*x
    x=num
    if amg==num:
        print("it is amstrong Number")
    else:
        print("Not amstrong number")
