#Implement python script to check the given year is leap year or not.
leap_year=366
not_leap_year=365
import datetime
y=datetime.datetime.now()
year1=y.year
if year1==leap_year:
    print("leap year")
else:
    print("not leap year")
print(y)