'''method override polymorphism'''



''' Example 1 '''

class vehicle():
      def start(self):
            print('Vehicle started')
class car(vehicle):
      def start(self):
            super().start() #calling first function if you want super keyword
            print("car started")
car1=car()
car1.start()   


'''Example 2'''

class ram:
    def project(self):
        print("Online Shopping Management System")

class sam(ram):
    def project(self):
        super().project()
        print("Online Voting System")

class kumar(sam):
    def project(self):
        super().project()
        print("Car Rental System")

obj = kumar()
obj.project()
