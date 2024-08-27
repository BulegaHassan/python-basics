# To work with dates we use the module datetime
import datetime
x = datetime.datetime.now()
print(x)
print(x.year,x.month,x.day)
# You can create a date with the datetime() constructor
y = datetime.datetime(1995,6,24)
print(y)
# To format the date we use strftime() method.
print(x.strftime('%B')) # month name, full version try replacing B with A,Y,y . See docs for more info
