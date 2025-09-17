import re
print("Welcome to Email Validator")



pattern ='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

user_id =input("Enter Your Email Id:")

if re.search(pattern,user_id):
      print("Valid Email ID")
else:
      print("Invalid Email ID")