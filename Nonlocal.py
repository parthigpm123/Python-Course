#nonlocal keyword uses to local keyword make nonlocal
def outer():
      msg='hello'
      def inner():
            nonlocal msg
            msg='hi'
            print(msg)
      inner()
      print(msg)
outer()      
            
            