#Append takes a single argument and adds it to the end of the list.

value=[1,2,3] # add last value only
value.append(4)

print('length',len(value))
print('minvalue',min(value))
print("max value",max(value))

#2.Extend takes an iterable (like a list, tuple, or string) as an argument and adds each element of that iterable to the end of the list.
nums= [1,2,3]
nums.extend([4,5,6])
print(nums)