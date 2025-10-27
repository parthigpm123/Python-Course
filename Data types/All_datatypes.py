
data_types_info = '''
Text Type:	       str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	      set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

'''

# Basic Data Types
a = 10               # int
b = 3.14             # float
c = 2 + 3j           # complex
d = True             # bool
e = "Python"         # str

# Sequence
f = [1, 2, 3]        # list
g = (4, 5, 6)        # tuple
h = range(5)         # range

# Mapping
i = {"name": "Parthiban", "age": 22}  # dict

# Set
j = {1, 2, 3}        # set
k = frozenset({4, 5, 6})

# Binary
l = b"Hello"         # bytes
m = bytearray([65, 66, 67])
n = memoryview(b"World")

# None Type
o = None

print(type(a), type(b), type(c))
print(type(f), type(i), type(j))
