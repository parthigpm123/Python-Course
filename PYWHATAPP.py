import pywhatkit
try:
  pywhatkit.sendwhatmsg("+916374570768","HELLO WORLD\n"*1000,22,6)
  
  print("successful send")
except:
      print("Something Went Wrong")