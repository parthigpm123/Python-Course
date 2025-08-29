import os

# remove file
os.remove("code2.txt")

'''
if os.path.exists("code2.txt"):
      os.remove("code2.txt")
else:
      print("FileNotFoundError")
      
'''    



# remove folder

# Note: You can only remove empty folders.

os.rmdir("demo folder")      