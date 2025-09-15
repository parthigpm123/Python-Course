import os

print("1.Shutdown")
print("2.Restart")
print("3.Exit")


Command =input("Enter Your Command :")

if "1" in Command:
      os.system("shutdown /s")
if "2" in Command:
      os.system("reboot")
if "3" in Command:
      exit()           