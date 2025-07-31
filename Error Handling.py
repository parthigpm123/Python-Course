'''
try:
  print(x+y)
except:
 print("an error occur")


#this block if you know correct value you can give here
try:
  
 usrname = input("Enter username : ")
 pwd     = int(input("Enter password : "))
 
 print("username :",usrname , "password:",pwd)
except:
 print("username password is incorrect") 
 
 
 


 
 #Runtime exception you don't know what will error presents ("Exception" keyword)
 try:
 a = int(input("give input=>👍 "))      
 
 print("answer",a)
except Exception as  e:
  print("Error message😨: ",e)
  

# if you know the correct errorname try this option (like zero division error,value error)
try:
    a = int(input("give input"))
    b = int(input("give input"))
    c = a / b
    print(c)
except ZeroDivisionError:
    print("don't enter 0 with any number for divide")
finally:
    print("exception was handled")    

    
    
# 2. multiple Except statement



try:
    a = int(input("give input for a ="))
    b = int(input("give input for b ="))
    add = a+b
    divide =a/b
    print("sum=",add)
    print("sum=",divide)
except ValueError:
  print("Enter only numbers") 
except ZeroDivisionError:
  print("not divided by zero")


# 3 (else)Try-except-else
#'else' only working try block not presents any error otherwise not work


try:
    a = int(input("enter no"))
    b = int(input("enter no"))
    
    print(a-b)
except: 
    print("Error Occurred")
else:
      print("result successful")    



#4 raise statement
#for manually  create any exception in programme or error name (Manual Error throw)

#syntax

age = int(input("enter your age : "))

if age<18:
  raise Exception("minor age not allowed")
else:
  print("you are allowed")

           
# 5try-except-finally 

'''
#a finally  clause always executed before leaving 
#the try statement whether an exception has occurred not 
 
'''     
'''

try:
  a = int(input("enter  a value"))
  b = int(input("give a value"))
  if a==b:
    print("two value is correct")
except:
  print("value error")
else:
  print("previous programme successful")  
finally:
  print("programme executed")    