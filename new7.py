#Unpacking a tuple:
    
"""""fruits = ("apple", "banana", "cherry")
(red,yellow,blue)=fruits
print(red,blue)""""""




"""""



#Assign the rest of the values as a list called "red":

    
fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruit

print(green)
print(yellow)
print(red)

#if we add star* while unpacking the started value will considered as a first value and formed as list




