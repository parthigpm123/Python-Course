"""FUNCTION ARE REFERENCE"""
"""function can return another function"""
def outer():
      x=5
      def inner():
            y=10
            res=x+y
            return res #this result store in inner func
      return inner()      #inner func store value int outer func 
a=outer()  #then outer function call
print(a)
  