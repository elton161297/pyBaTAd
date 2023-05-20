#Print the second item in the tuple:
    
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


""""""

#Check if "apple" is present in the tuple:
    
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("yes")
    
""""""

#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y=list(x)
y[2]="pineapple"
x=tuple(y)
print(x)

""""""

#Create a new tuple with the value "orange", and add that tuple:

tuple = ("apple", "banana", "cherry")
z="orange",
tuple+=z
print(tuple)



