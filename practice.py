'''
a = 10
if 10<a:
      print("smaller than a")
elif 10>a:
      print("greater than a") 
else:
      print("both are equal")



A = {'apple' , 'orang' , 'banana'}
b= {"pineapple","orang", "mango","kiwi"}

A.update(b)
print(A)      


A ={ 1,2,3}
b= {4,5,6}

A.update(b)
print(A)
 '''

#thislist =list( 'apple ','orange','kiwi','mango')
#print(type(thislist))


'''
set1 ={
      "name": "parthiban"
}

x=set1.get('name')
print(x)


set1 = {
      "name": "Name========> parthiban "
        
      }
x = set1.get("name")
print(x)


username = "parthiban"
password = 12345  

uname=input("Username : ")
pwd = int(input("password : "))

def myfunc():     
      print(username==uname and password==pwd)
      
myfunc()
'''

username = "parthiban"
password = 12345  

uname=str(input("Username : "))
pwd = int(input("password : "))

def validate():
      if(username==uname and password==pwd):
       print("both are same")
      else:
       print("not true")
validate()
             

