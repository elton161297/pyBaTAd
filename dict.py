fruits={"apple":10,"bananna":20,"cherry":30,"avacado":40,"pineapple":50}

for key,value in fruits.items():
  print(key,value)
  fruits.update({key:value+10})
  


print(fruits)

 


