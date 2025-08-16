
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

'''
Date Formats
Code	Meaning	           Example
%Y	Year (4 digits)	     2025
%y	Year (2 digits)	     25
%m	Month (01–12)	     08
%B	Full month name	     August
%b	Short month name	     Aug
%d	Day of month (01–31)   14
%j	Day of year (001–366)  226
%A	Full weekday name	     Thursday
%a	Short weekday name     Thu
%w	Weekday number         (0=Sunday)	4
'''
'''
Time Formats
Code	Meaning	      Example
%H	Hour (24-hour)	15
%I	Hour (12-hour)	03
%p	AM / PM	PM
%M	Minutes (00–59)	45
%S	Seconds (00–59)	09
%f	Microseconds (000000–999999)	573829
'''

#date format strftime
import datetime
x = datetime.date.today()
y=datetime.datetime.now()
print(x.strftime('%a-%b-%y'),y.strftime('%I:%M:%S %p'))

print(x.strftime('%A-%B-%Y'),y.strftime('%I:%M:%S %p'))

#time format strftime
from datetime import datetime
ctime =datetime.now().time()
print("12 hours format",ctime.strftime("%I:%M:%S %p %f" ))

print("24 hours format:",ctime.strftime("%H"))
