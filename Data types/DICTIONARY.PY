'''
✅ Common Dictionary Methods

Method	Description

dict.get(key)	Returns value or None (optional default)

dict.keys()	Returns a view of keys

dict.values()	Returns a view of values

dict.items()	Returns a view of (key, value) pairs

dict.pop(key)	Removes key and returns value

dict.update(dict2)	Updates with another dictionary

dict.clear()	Removes all items

dict.copy()	Returns a shallow copy
'''


'''My_details=int({
      "Name": "parthiban",
      "Age":  2,
      "City": "chennai"
})

for x in My_details:
      print(My_details)
'''      
      
map = {1:"one", 2:"two", 3:"three"}

print(type(map))

print(map[1])
print(map[2])
print(map[3])      

#string value can provide

b={"1":"one", "2":"two", "3":"three" }

print(b["1"])


#tuple in dict
tup={1:(1,2,3),2:(4,5,6)}

print(tup[1])

#set in dict
set1 ={1:{1,2,3,4},2:{5,6,7,8}}
print(set1[1])

#list in dict
lst1={1:[1,2,3,4],2:[5,6,7,8]}
print(lst1[1])
print(type(lst1))

#Get method

set1 = {
      "name": "Name========> parthiban "
        
      }
x = set1.get("name")
print(x)
'''
#pop() remove key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)
'''

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()



#update() method
print(car)

mycar ={
      "name": "lamborgini"
}

mycar.update({"year":2034})

print(mycar)


#len() method
print(len(mycar))


#keys function find out key only
name1 = {
      1 : "parthiban",
      2 : "karthick"
}

print(name1.keys())
print(name1.values(   ))


#item() print all key and value in
# 
print(name1.items())


#insert per key
name1[3] = "john"
print(name1)
