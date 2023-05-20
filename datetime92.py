import datetime
a=datetime.datetime.now()
print(a)
print(a.year)            #for print the year
print(a.strftime("%A"))  #for print day
print(a.strftime("%B"))  #for print month 

#Creating datetime Manually
b=datetime.datetime(1997,12,16)
print(b)