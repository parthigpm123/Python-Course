#use to join  integer and strings

a = 10
b = f' my age is {a}'
print(b)


x = 100
y= f'the car price is {x} dollars'
print(y)

delivery_partner="swiggy"

def hotel():
      item = 'pizza'
      
      def order():
            quantity =2
            print(f"ordering {quantity} {item} using {delivery_partner}")
      order()
   
hotel()           

