'''

The enumerate() function in Python is a built-in function that adds a counter to an iterable and returns an enumerate object. This object can then be used in a loop to access both the index and the value of each item in the iterable.
''' 
#basic syntax
'''enumerate(iterable, start=0)'''

lst =[ "💖", "💖💖","💖💖💖"]

print(list(enumerate (lst,start=1)))


#for loop  enumerate
for index,value in enumerate(lst,start=1):
      print(index,value)
      
