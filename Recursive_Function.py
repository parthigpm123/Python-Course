'''
Recursive Basic Function

two types

1.base Case => when stops comes zero

2.Recursive Case=> function call itself given argument 

'''
# Basic Function
def hi(n):
      if n!=0: #base case = stop function when come zero
       print("python",n)
       hi(n-1)  # Recursive
          
hi(10)                     

'''
Answer
python 10
python 9
python 8
python 7
python 6
python 5
python 4
python 3
python 2
python 1

'''