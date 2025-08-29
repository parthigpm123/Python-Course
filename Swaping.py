'''
variable data swapping
'''
#easy method
a = 5

b = 10

a ,b = b ,a

print(a,b)

# this is  wrong  method-----------------------------------------------------------------
x=10

y= 9

temp = x

x =y

y = temp
print(x,y)