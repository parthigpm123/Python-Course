#Iterator use to print index value one by one with next inbuilt function

'''
iterator have two Inbuilt functions

1 iter() create iterator from iterables 

iterator is an object tah contains countable number of values

use to create an iterator from any iterable list,tup,set,str,int


2 next() get next item from iterator

use to get or print next iterator from an object

#save memory memory efficient 

#access item from list without any for loop and indexing method

# one element only print at moment  


'''



lis = [1,2,34,4,5]

it= iter(lis)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#class type ietrator
print(type(it))

lst =["python","hello","world","fantastic","super"]

itr =iter(lst)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


#access index value by index slice

lst1 =["python","hello","world","fantastic","super"]

print(lst1[0])
print(lst1[1])
print(lst1[2])
print(lst1[3])
print(lst1[4])


#using for loop print one by one
lst2 =["python","hello","world","fantastic","super"]
for i in lst2:
      print(i)



#now use iterator 





