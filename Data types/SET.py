'''
Set Methods

Python has a set of built-in methods that you can use on sets.

Method	Shortcut	Description

add()	 	Adds an element to the set

clear()	 	Removes all the elements from the set

copy()	 	Returns a copy of the set

difference()	-	Returns a set containing the difference between two or more sets

difference_update()	-=	Removes the items in this set that are also included in another, specified set

discard()	 	Remove the specified item

intersection()	&	Returns a set, that is the intersection of two other sets

intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

isdisjoint()	 	Returns whether two sets have a intersection or not

issubset()	<=	Returns whether another set contains this set or not

 	<	Returns whether all items in this set is present in other, specified set(s)
  
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
  
pop()	 	Removes an element from the set

remove()	 	Removes the specified element

symmetric_difference()	^	Returns a set with the symmetric differences of two sets

symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another

union()	|	Return a set containing the union of sets

update()	|=	Update the set with the union of this set and others
'''



'''# add method
set1={1,2,3,4,4,5}
set1.add('9')
print(set1)

#set1.remove(1)
set1.add(True)

print(set1)

'''

'''
# clear() method
A={1,2,3,4,5,6}

A.clear()
print(A)

#copy() method
x={1,2,3,45}

y=x.copy()
print(y)

#discard()
a={1,2,3,4,5,6}

a.discard(1)
print(a)
'''

#Update method

z={1,2,3,4,5,6,}
y={10,20,30}
y.update(z)
print(y)

#pop() method
c={1,2,3,4,5,6}
c.pop()
print(c)

#union( method )

a={1,3,4,5,6}
b={20,30,40}
a.union(b)
print(a)
      
'''     
a = {'apple' , 'orang' , 'banana'}
b= {"pineapple","orang", "mango","kiwi"}

a|=b
print(a)            
      
      
set3 ={1,2,3,4,5,6}

set3.discard(1)      

print(set3)
'''


      