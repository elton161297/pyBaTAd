# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json
a= '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
print("The original string : " + (a))
print(type(a))
res = json.loads(a)
print("The converted dictionary : " + str(res))
print(type(res))