
'''
1. File and Directory Management:
Creating directories: Use os.mkdir() to create a single directory or os.makedirs() to create nested directories. 
Deleting directories: os.rmdir() removes an empty directory, while os.removedirs() removes nested directories recursively. 
Renaming files and directories: The os.rename() function can change the name of a file or directory. 
Listing files and directories: os.listdir() returns a list of files and directories within a specified path. 
Changing the current working directory: Use os.chdir() to navigate between directories. 
Getting the current working directory: os.getcwd() returns the path of the current working directory. 
Checking if a path exists: os.path.exists() verifies the existence of a file or directory. 
'''



import os
#print(dir(os))

#print("working directory:",os.getcwd())

print("list", os.listdir("C:\\Users\\parthibantech\\Desktop\\Python_Learn\\Python-Course"))