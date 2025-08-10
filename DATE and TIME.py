
from datetime import datetime

x=datetime.now()

print(x)



#find out current date syntax
print("Today Date")
import datetime

y=datetime.date.today()
print(y)

print("Date: ", y.day)
print("Month:",y.month)
print("Year: ", y.year)




#find out current time
import datetime

# Get current time
print("Indian current time")
d = datetime.datetime.now().time()

print(d)

print("Hour:  ",  d.hour)
print("Minute:",d.minute)
print("Second:",d.second)



import time 
x =time.time()
print(time.ctime(x))