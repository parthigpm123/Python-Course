'''
The random module in Python is a built-in library that provides functions for generating pseudo-random numbers and performing random operations. It is widely used in various applications such as simulations, games, randomized testing, and data science.

games most used
1. dice rolls
2. shuffle cards
3.enemy movement in games
4.ludo ,snake ,ladder,poker ,lottery, otp
'''
import random as r

Random_Number=r.randint(1,10)

random_range=r.randrange(1,100,2)

print("Random Number :",Random_Number)

print("Random_Range : ",random_range)

# 3 decimal random number (0.0 to 1.0)
Random=r.random()
print("Random_Random : ",Random)

#4 random choice from a list

lst1=["apple","banana","orange","grape"]

fruit=r.choice(lst1)

print("best random fruit :",fruit)

#5shuffle a list

shuffle1=[1,2,3,4,5,67,]

r.shuffle(shuffle1)

print(shuffle1)