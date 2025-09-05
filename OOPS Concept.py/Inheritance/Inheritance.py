'''there is 5 type of Inheritance

1 Single Inheritance

2 Multiple Inheritance

3 Multi-level Inheritance

4 Hierarchy Inheritance

 Hybrid Inheritance

'''
'''
#single inheritance
class dad():
      def phone(self):
            print("This dad's phone")

class son(dad):
      def money(self):
            print("This is my money")

ram=son()

ram.phone()
ram.money()     
'''

#multiple inheritance
'''
class dad():
      def property(self):
            print("This is Dads property")
class mom():
      def car(self):
            print("This is mom's Car")
class son(mom,dad):
      def ball(self):
            print("this is my ball")
vijay=son()
vijay.property()
vijay.car()
'''

#Multi-Level Inheritance
'''
class grandpa():
      def phone(self):
            print("This is grandpa phone")                        
class dad(grandpa):
      def money(self):
            print("This is dads money")               
class son(dad):
      def laptop(self):
            print("This is my laptop")
sam=son()
sam.money()       

dad1=dad()
dad1.phone()                              
sam.phone()            
'''

#Hierarchy Inheritance

class dad():#parent Class
      def money(self):
            print("this is dads money")
class son1(dad):#child class
      pass

class son2(dad):
      pass
class son3(dad):
      pass            
s1=son3()
s1.money()                        
            
                        
            
