# text mode ===> default mode
# binary mode for images and videos 

'''

File is not present --> FileNotFoundError

w --> write operation. Existing content of the file will be overridden.

File is not present --> This will create a new file

a --> It opens an existing file for append operation. It wont override existing content.

File is not present --> This will create a new file.

r+ --> Read and Write Data into the file. Existing content will not get deleted.

w+ --> To Write and Read data from the file. It will override existing content.

a+ --> To append and Read Data from the file.

X --> Exclusive Operation

If file is already present, it will throw FileExistsError

'''
''' print(f.tell()) #find the cursor position'''

'''print(f.seek(0)) # move cursor position'''

file = open('code.txt','r+')

#print(file.read())
#basic functions
print("file mode====>",file.mode)
print("file name====>",file.name)
print("file property====>",file.readable())
print("file writable====>",file.writable)
print("file closed or not====>",file.closed)


print("file closed or not====>",file.closed)

#write mode
file.write("python is awesome\n")

file.write("i love gaming\n")

#file=open("code.txt","a+")
file.write("ppppp\n")
#


#list add in file
lst=[" parthiban  ","vijay  ", "balaji  ","arul \n"]
file.writelines(lst)
file.seek(0)

#read all data from file 
print("read all===>",file.read())
file.seek(0)

#only one line read
print("One line only====>",file.readline())
print("cursor position===>",file.tell())  
#read all line in list format
file.seek(0)
print("list format===>",file.readlines())


# with statement to open file 

#important point
'''you dont need to close the file manually. it will auto close once operation done'''

with open("code.txt","r") as f:
      print(f.read())


# new txt file create method      
with open("code2.txt","x") as cod2:
      cod2.write("hello world")
 
 
 
# binary format open video image and audio      
#with open("god.jpg","rb") as h:
      #print(h.read())      