'''A regular expression (shortened as regex or regexp), sometimes referred to as a rational expression, is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

 1 Email Validation
2.phone number validation 
3.URL validation 
'''


import re

text= "the rain in spain"

a=re.search("spain$",text)

print(a)

if a is not None:
      print("match found!!!!!!")
else:
      print("match not found!!!")
      
pattern =r"apple"      
text1 ="apple.pie"

match=re.match(pattern,text1)
print(match)

if match:
      print("match found")
else:
      print("not found")