import datetime
x = datetime.date.today()
y=datetime.datetime.now()
print(x.strftime('%a-%b-%y'),y.strftime('%I:%M:%S %p'))
