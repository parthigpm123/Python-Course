'''In Python, an assert statement is like a built-in "sanity check" for your code. It's a way to confidently state that a certain condition must be true at a particular point in your program's execution.'''
#like as exception handling

def age(value):
    assert value>0,'please enter valid age'
    print('Your age is:',value)
ag=int(input("Enter Your Age:"))
age(ag)    