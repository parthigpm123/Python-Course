'''
print function  4 types   1.sep 2.end  3.file  4.flush

 syntax print function==>print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) 

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
'''

'''
0. object mean what  give into print function

eg. print(10,"hello") like this 
'''
print("hello world",end=" ")

print("python is awsome")

print("hello python", "is awesome","super",sep="***")
# ans hello python***is awesome***super

'''
1.sep parameter is used to separate the value with given any symbol

default  value a space.
'''
print("A", "B", "C", sep="-")

# answer> A-B-C

print("apple", "banana", "cherry", sep="......")

print(1,2,3,4, sep=",")


#----------------------------------------------------#

'''
2. End 

end decides what comes after your printed text.
Default is newline (\n), but you can change it to space, comma, dots, or anything else.

default value is a newline(\n)


'''

print(1,2,3,4,5,sep=",",end="......")

print(8,9,10,sep=",")

# answer 1,2,3,4,5......8,9,10

print("hello",end=" world ") # append any value

print("python")

# answer = hello world python
#-----------------------------------------------------




'''
Defaults to the current sys.stdout.

3.file parameter in print function is used to explicitly specify the file

where the given values to be printed should be written to.

# Default value of file parameter is sys.stdout

'''
file1 =open("Print_Function/text.txt","w")
print("python is awesome ",file=file1)
file1.close()

# Default path  text file will create ==> PS C:\Users\parthibantech\Desktop\Python_Learn\Python-Course



#-----------------------------------------------------#
'''
4.flush default value=False

Meaning of flush in Python print()

Flush = forcefully empty the buffer (send the output immediately).

Normally, Python doesn’t always write to the screen/file instantly. It first stores text in a temporary memory area called a buffer.

When the buffer is full (or when a newline \n comes), Python "flushes" (empties) that buffer to the output (screen/file).

print("Hello", end="", flush=True)  


 
'''
print("Hello", end="", flush=True)  
 




# help to see all print function parameter 
#help(print)