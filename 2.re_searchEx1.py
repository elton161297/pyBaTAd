#search function


import re

line = "Cats are smarter than Dogs"


searchObj = re.search(r'(.*) are (.*?) (.*)', line, re.M|re.I)
print(searchObj)


if searchObj:
    print ("searchObj.group() :", searchObj.group())
    print ("searchObj.group(1):", searchObj.group(1))
    print ("searchObj.group(2):", searchObj.group(2))
    print ("searchObj.group(3):", searchObj.group(3))
else:
    print ("Nothing found")
