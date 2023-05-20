#Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
            # Unit                                                     Price  
       #First 100 units                                               no charge
       #Next 100 units                                              Rs 5 per unit
       #After 200 units                                             Rs 10 per unit
       #(For example if input unit is 350 than total bill amount is Rs2000)

a=int(input("Enter the usage"))
if a<100:
    print("no charge for you")
elif a<200:
     print ("than total bill amount is: RS ",a*5)
elif a<300+a:
     print ("than total bill amount is: RS ",a*10)

    