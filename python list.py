#list store value of int,
#bool value ,string value  we  can make duplicate, changeable,

# Built-in functions

# 1 len() find out how many character in the sequence

# 2 append() add value to end of list take one arguments only otherwise error

# 3 extend()  add whole list value
# 4 insert() add value index position
# 5 .clear() delete list item

# 6. count() function use to how many  same value in the list

# 7 index() function find out index position

# 8 min and max elements find out

# 9 ls2.sort() default (ascending) function used to  list item ascending 

# 10 ls2.sort(reverse = True) use to descending

#11 print(sum()) add value in sequence

#12 ls2[0] =100 change one index value in the list


# delete function 

# 1 pop() delete index value

# 2 .remove()

# 3.clear() delete all item

# nested list (append)

lst1 = [1,2,3,4,56,7]
print(len(lst1)) #===len function

#_______________________________________________________________#

lst1.append(2 )
print(lst1) #===append function

#_______________________________________________________________#
lst2=[1,2,3]

lst3 = ['parthiban'] #====> extend function
lst2.extend(lst3)
print(lst2)

#___________________________________#

lst4 = [1,2,3,4,5]

lst4.insert(0 ,0)
 
print(lst4)

#________________________#

#nested list (append)

lst5= [1,2,3]

lst6 =[7,8,9]

lst5.append(lst6)

print(lst5)

#__count__

ls2 =[1,1,1,1,1,1]

ls2.count(1)

print(ls2.count(1))

#_________________

#index()

ls3 = (1,2,3,4,5,6)

print(ls3.index(5))

#_______________#

#min and max elements find out

ls4=[1,10,3,4]

print(min(ls4))

print(max(ls4))

#___________________
#sum add all value

ls5 = [10,10]
print(sum(ls5))

ls5[0] = 100
#


#delete index position value pop() default value -1
ls6 = [1,2,3]
ls6.pop(2)
print(ls6)


#delete data position value .remove()
ls7 =[1,3,34,4,5,6,7,]
ls7.clear()
print(ls7)

#nested list

ls1=[[1,2,2],[4,5,6,7]]
print(ls1[1])

print(ls1[1][0])






















































 




