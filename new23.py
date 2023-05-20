#Write a program to accept a number from 1 to 7 and display the name 
#of the day like 1 for Sunday , 2 for Monday and so on.

days=str(input("Enter The Day -- "))
sunday="sunday"
monday="monday"
tuesday="tuesday"
wednesday="wednesday"
thursday="thursday"
friday="friday"
saturday="saturday"

if days==sunday:
 print("1")
 
elif days==monday:
 print("2") 
 
elif days==tuesday:
 print("3") 

elif days==wednesday:
 print("4") 

elif days==thursday:
 print("5")

elif days==friday:
 print("6")

elif days==saturday:
 print("7")

else:
 print("Check The Spelling You Entered")