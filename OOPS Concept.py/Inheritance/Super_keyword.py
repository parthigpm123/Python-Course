                      
class A():
      def __init__(self):
            print("print from a class")
      def greet(self):
        print("Hello from A")

class B():
      def __init(self):
            print("print from b class")
            super().__init__()
      def greet(self):
        print("print from b class")
# Call greet() from A

class C(A):
      def __init__(self):
            super().__init__()
            print("Print from c class")
            
  # Call greet() from B

obj = C()
obj2 = B()
obj2.greet()


