'''
python modules is collection of functions and classes , variables

you can import another  file with in same folder

file name should be ==> mymodule.py extension name set


=> reusability once you define function or classes within module 
you can easily reuse  them in another part of program  or even completely different project

=> this avoid code code duplication


**type of module **

1. User  define module
these module created ny developers to organize their code

reuse save it .py   
---------------------------
2.Built in modules
1 math   2 random   3 os 4 date time  
---------------------------
3.Third party (not created by python )
1 numpy 2 pandas 3 matplotlip

4 request for https 5 flask/django
'''

# "as" key word use to change file name 












from  mymodule import greeting as greet

greet(" parthiban ")

#you can directly access function which you want instead of import whole function  

from mymodule import add as a

a(10,10)

# define function in mymodule import here then reuse the function 
import mymodule

ans =mymodule. module(10,50,10,20)

print(f"The result is:{ans}")

