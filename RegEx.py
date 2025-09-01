'''A regular expression (shortened as regex or regexp), sometimes referred to as a rational expression, is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

 1 Email Validation
2.phone number validation 
3.URL validation

important func

1 match() ==> Give output only beginning of given string

2 search()==> give out put search anywhere from the string line

3 findall() ==>  search and match process find how many str in given line

4 finditer find all str word index position 
'''
import re

#match
print("\n Match Function")
result=re.match(r"python","python is awesome")

print("Match Function Result==>",result.group())

# find first letter in that line


#----------------------------------------------------#

#2 search
print("\n Search Function")

Rslt = re.search(r"coding"," is awesome coding")

print("Search function Result==>",Rslt.group())


# 3findall()

print("\n Findall Function")

result1=re.findall(r"is","python is awesome is python")

print("Findall Func Result==>",result1,)



#4. finditer
count1 = 0
print("\n Finditer Function")

result2=re.finditer(r"python","python is awesome,python is good")

for i in result2:
      count1+=1
      print(count1,"Find all result==>",i.group(),"at",i.span())

#print("Find iter result==>",result2)

print(" ")























'''
🔹 Regex Quick Guide

\A → Match only if pattern is at the start of the string

\b → Match at a word boundary (start or end of a word)

\B → Match when it’s not at a word boundary (inside a word)

\d → Match a digit (0–9)

\D → Match anything that is not a digit

\s → Match a whitespace (space, tab, newline)

\S → Match a non-whitespace character

\w → Match a word character (a–z, A–Z, 0–9, _)

\W → Match a non-word character (symbols, punctuation, etc.)

\Z → Match only if pattern is at the end of the string
'''



import re

'''
#1. search function

text= "the rain in spain"

a=re.search("spain$",text)

print(a)

if a is not None:
      print("match found!!!!!!")
else:
      print("match not found!!!")



#2match function

      
pattern =r"apple"      
text1 ="apple.pie"

match=re.match(pattern,text1)
print(match)


if match:
      print("match found")
else:
      print("not found")
'''      


pattern = r"\d+"


text=" There are 100 apples"

match=re.search(pattern,text)

print("match func result=>",match.group())

