import re

txt="python is easy to learn"
t1=re.match(r'python',txt)
if t1:
    print("match found ",t1)
else:
    print(t1, "match not found")