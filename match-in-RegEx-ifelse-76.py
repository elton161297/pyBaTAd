import re

txt="python is easy to learn"
t1=re.match(r'python',txt)
if t1:
    print("match found ")
else:
    print("match not found")