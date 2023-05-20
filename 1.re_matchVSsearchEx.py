import re

line = "Cats are smarter than Dogs"

matchObj = re.match (r'cats', line, re.I)

if matchObj:
    print ("Match is success")
else:
    print ("Match is Not success")

searchObj = re.search (r'Dogs', line, re.I)

if searchObj:
    print ("Search is success")
else:
    print ("Search is Not success")
