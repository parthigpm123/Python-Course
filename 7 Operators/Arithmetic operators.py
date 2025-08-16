# This is  7 Type of operators in python


# 1 arithmetic operators addition(+) கூட்டல் 
x=10 
y=10
z=20
print(x+y+z)

# 2 arithmetic operator subtraction(-) கழிதல் 
a=10
b=5
c=20
print(a-b-c)

# 3 (*) multiplication பெருக்கல் 
e = 10 
f =4
print(f*e)

# 4 (/) division show decimal ( float value)value வகுத்தல்  
g =2
h = 2 
print(g/h)


# 5 (%) modulus  மீதம் 
name = 10
age = 3
print(name%age)

# 6 floor division(//) ( show  integer value) முழு வகுத்தல் 
n =100
p= 10
print(n//p)

print(n//p)

# 7 (**) Exponentiation in  அடுக்குகள் 
a =10 #==>base value
b = 2  #======> exponent value  10x10=100 10 times multiple 10
print(a**b)

# Division and Floor Division Examples

# List of pairs to divide
examples = [
    (10, 3),
    (9, 2),
    (15, 4),
    (20, 5),
    (7, 7),
    (14, 3),
    (5, 2),
    (8, 4),
    (19, 6),
    (25, 8)
]

print("Division and Floor Division Results:\n")

for num1, num2 in examples:
    division = num1 / num2
    floor_division = num1 // num2
    print(f"{num1} / {num2} = {division}")
    print(f"{num1} // {num2} = {floor_division}")
    print("-" * 30)
