'''__name__: This variable holds the name of the current module. Its value changes based on how the script is being executed:
If the script is run directly, __name__ is set to "__main__". '''


print("This is value of:",__name__)

def add(x,y):
      print(x+y)

if __name__ == "__main__":
   add(2,4)
   
   print(__file__)
   print(__package__)