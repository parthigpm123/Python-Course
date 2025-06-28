#positional arguments in python
def add(no1,no2):#========>parameters 
    print(no1,no2)
add(3,no2=5)#=======>arguments
    
     
def my_func(str,num):
    print(str*num)
my_func("python is awesome",5)    


#keyword arguments syntax
# order of arguments can be changed
def add(no1,no2):#========>parameters 
    print(no1 , no2)
    print(no1 + no2)
    print(no1 - no2)
    print(no1 * no2)
add(no2=3 , no1=3)#=======> arguments passed in order of parameter name
    
    
#default arguments
def login(username="admin" ,pwd="test"):
    print(username, 'logged in successfully', pwd)

login("parthiban",1234) #default arguments

  
login(username="me" ,pwd = "me") #keyword arguments 

login("parthiban" , pwd=1234) # positional with keyword argument    

login(pwd=1234)

login("parthiban")