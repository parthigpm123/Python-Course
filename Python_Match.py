''' Match statements use instead of If-Else'''

'''
1.match

2.case

3.| ==equal or symbol

4case _:  #default case
 print("unknown numbers")
'''
day=7

match day:
      case 6|9|10:
            print(day," equal")
      case 7:
            print(day,"equal to 7")
      case 4:
            print(day,"equal to4")            
      case _:
            print(day,"Unknown Numbers")

#-------------------------------------#

number=int(input("Enter Number:"))            
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
#--------------------------------------#    
    
    month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

            
            
