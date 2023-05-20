#Write a program to accept percentage from the user and display the grade according to the following criteria:

         #Marks                                    Grade
         #> 90                                       A
         # > 80 and <= 90                            B
         #>= 60 and <= 80                            C
         # below 60                                  D
         
a=int(input("enter the marks:  ")) 
#print("Grade A") if a>90 else(print("your marks is below 90"))     
#print("Grade B") if a>80 or a<=80 else(print("your marks is below 80"))         
#print("Grade C") if a>=60 or a<=60 else(print("your marks is below 80"))         
#print("Grade D") if a<60  else(print("your marks is below 60"))  

if a>90:
    print("Grade A")
elif a>80:
    print("Grade B")
elif a>= 60:
    print("Grade C") 
else:
    print("Grade D")    

   