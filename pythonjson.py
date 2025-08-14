'''
JSON - javascript object notation (key value pair)

=> A light weight format for store and exchange data

=> it's text format both human and computer readable easily

=>Widely Using web development and other application

=>before using(XML, CSV) format not now

=> this is language independent(all java , python ,javascript)

'''


'''
two methods 

1. json.dumps()

=>python object convert to json string

if you have any python data format  you can convert  json string format
---------------------------------------------------------------------------------
2.json.loads

=> json string(str)  to python object(dict)

if you have any json string you can convert to python object(dict)
''' 

#1 json.dumps (python object to json str)

import json

x={
      "name" :"parthiban",
      "age"  :24,
      "place":"chennai",
      "job"  :"python developer"
}

print(type(x))
y=json.dumps(x)

print(y)
print(type(y))


#json.loads (json string to python object Dict)

js='{"name": "parthiban", "age":24, "place":"chennai", "job":"python developer"}'


print(type(js))
pydict=json.loads(js)

print("Result=>",pydict["name"])
print(pydict,type(pydict))


'''
when you converted from python to json

python                 json

1 dict                  object

List                    array

tuple                   array

str                     str

int                     number

float                   number

true                    true

false                    false

none                     null 






'''