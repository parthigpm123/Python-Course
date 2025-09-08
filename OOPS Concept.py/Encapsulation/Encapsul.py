'''
=> Binding data and functions into single entity or capsule

=>data hiding
=>data bundling
=>data private and protect

1.Public= access by any functions and classes
2.Protect= Accessed by only parent class or and child class inherits
3.Private= Accessed by only parent inside class and parent inside methods 


Single underscore _ → “protected” by convention.

Double underscore __ → triggers name mangling, making it harder (but not impossible) to access from outside.

Methods
1.setters
2.Getters

'''

''' 1.Public= Public= access by any functions and classes '''
class company():
      def __init__(self):
            self.companyname='Public google'#Public Attributes
      def companynm(self): #methods
            print(self.companyname)     
obj=company()
obj.companynm() 


'''2.Protect= Accessed by only parent class or and child class inherits '''

class company():
      def __init__(self):
            self._companyname='Protect google'#Private Attributes
            
class access(company):
      pass
      #def display(self):
            #print(self._companyname)
                             
obj=access()
print(obj._companyname)        


''' 3.Private= Accessed by only parent inside class and parent inside methods '''
class company():
      def __init__(self):
            self.__companyname='Private google'#Private Attributes
            
      
      '''Getters called get the private attribute value using create inside def method'''
      def companynm(self): #methods
            print(self.__companyname)
      '''Setters'''
      def setter(self):
            pass        
obj=company()
obj.companynm()     



  
