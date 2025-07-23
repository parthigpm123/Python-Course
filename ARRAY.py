
#METHOD ONE
import array as arr

x = arr.array("i",[1])
print(x)


#METHOD TWO
#LOOP IN ARRAY

from array import*
vals=array('i',[10,20,30,10])
for val in vals:
      
      print(val)
 #length     
print("length of array==>",len(vals))   

#append one element only
vals.append(40)
print(vals)


#extend more element add in array

vals.extend([80,90,70])
print(vals)

# count how many charecter in the  same  in the sequence     
print(vals.count(10))

#insert add index value
vals.insert(0,100)
print(vals)


#pop() delete index position value
vals.pop(0)
print(vals)

#remove() elements

vals.remove(80)
print(vals)

#acces index value
print(vals[0])

     
      
      