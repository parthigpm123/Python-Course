import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

'''# display the one month calendar'''
calendar=calendar.month(year, month,w=5)
print("\n", calendar)


