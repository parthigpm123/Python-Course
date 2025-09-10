'''nested means  function inside a function '''

def outer():
      name='vijay'
      def inner():
         nam="john"
         def  nest():
               n="vicky"
               print(n)
         nest()
         print(nam)
      inner()   
      print(name)
outer()      
              
                  
                  
def outer():
      x=5
      def inner():
            y=10
            res=x+y
            return res #this result store in inner func
      return inner()      #inner func store value int outer func 
a=outer()  #then outer function call
print(a)
  