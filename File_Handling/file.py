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
file.write("python is awesome")

file.write("i love gaming")

#file=open("code.txt","a+")
file.write("ppppp\n")
#


#list add in file
lst=[" parthiban  ","vijay  ", "balaji  ","arul \n"]
file.writelines(lst)


# all text file read
read1=file.read()

print(read1)

