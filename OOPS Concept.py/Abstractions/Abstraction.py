'''
Abstraction in Python, a core principle of Object-Oriented Programming (OOP), involves handling complexity by hiding unnecessary details and exposing only the essential information to the user. It allows developers to focus on what an object does rather than how it 
achieves its functionality. 

Note: Abstract class cannot be initiate or cannot be  create object
'''

from abc import ABC, abstractmethod

'''abstract class  cannot be accessed   '''
class animal(ABC):
      @abstractmethod            
      def sound(self):
            pass
      
      @abstractmethod
      def legs(self):
            pass


'''Child class  '''     
class dog(animal):
      def sound(self):
            print("I Bark")
       
      def legs(self):
            print("I Have Four Legs")
                  
obj=dog()
obj.legs()
obj.sound()            