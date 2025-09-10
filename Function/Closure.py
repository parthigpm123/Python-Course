def outer():
      msg=5
      def inner():
            print(msg)
      return inner
obj=outer()
obj()      