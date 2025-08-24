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

file = open('File_Handling/code.txt','r')

print(file.read())
file.close()

