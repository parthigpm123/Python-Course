'''sys module mainly contribute  interpreter and  programming'''


import sys

print("The Limit Of Recursion:",sys.getrecursionlimit(),"Time Only Will repeat")




# 1 find os platform
print("OPERATING SYS PLATFORM",sys.platform)

#--------------------------------------#

#2 find system information
import sys
print("System Information==>",sys.version)

#---------------------------------------#
#3 exit function
import sys
print("Hello")
#sys.exit()
print("This will not run")

#4 print all path
import sys
print("System Path=>",sys.path)

#5 show all function
print("SHOW ALL FUNCTION",dir(sys))

print(  )


# find where python installed path
syst=sys.path

for i in syst:
      print("LIST OF PATH",i)



