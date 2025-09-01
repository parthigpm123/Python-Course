'''
pass


jump statement used to inside function or
conditional statement 
'''
if 10==11:
      pass

#------------------------------------------------------------#

'''
two types of jump statement

1. continue ======> it will skip the value 
2. break===========> it will terminate the loop
'''      

      
for i in range(1,11):
      if i==3:
       continue# it will skip 3 value
      if i==8:
            break
      print("continue statement==>",i)    
      
  
while True:
      print("infinite loop\n")
      break# it will terminate the infinite loop      

print("loop terminated\n")      

#------------------------------------------------------------#

#for loop with else
for y in range(10):
      print(y)
      if y==5:
            break
else:
      print(" executed when loop is not terminated by break statement")      
      
      
      
      


