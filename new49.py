n=int(input("Enter The students ID -- "))
dic={}
for i in range(n):
    name=input("Enter Student Name -- ")
    marks=input("Enter Student Marks -- ")
    dic[name]=marks
    
while True:
    name=input("Enter Student Name To Get Marks -- ")
    marks=dic.get(name,-1)
    if marks==-1:
        print("Student Not Found")
    else:
        print("The Marks Of ",name,"are",marks)
    option=input("Do You Want To Find Another Student Marks [YES][NO]")
    if option=="No":
        break
print("Thanks For Using Our Application")