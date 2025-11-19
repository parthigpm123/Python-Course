# ---------------------------
# CASE CONVERSION METHODS
# ---------------------------

print("Hello".lower())            # hello
print("hello".upper())            # HELLO
print("hello world".title())      # Hello World
print("python programming".capitalize())  # Python programming
print("PyThOn".swapcase())        # pYtHoN


# ---------------------------
# SEARCH & COUNT METHODS
# ---------------------------

print("hello".find("l"))          # 2
print("hello".rfind("l"))         # 3
print("hello".index("e"))         # 1
print("banana".count("a"))        # 3


# ---------------------------
# BOOLEAN CHECK METHODS
# ---------------------------

print("python".startswith("py"))  # True
print("python".endswith("on"))    # True
print("abc123".isalnum())         # True
print("abc".isalpha())            # True
print("123".isdigit())            # True
print("hello".islower())          # True
print("HELLO".isupper())          # True
print("Hello World".istitle())    # True
print("   ".isspace())            # True


# ---------------------------
# MODIFY OR REPLACE TEXT
# ---------------------------

print("hello world".replace("world", "Python"))  # hello Python
print("  hello  ".strip())       # hello
print("  hello".lstrip())        # hello
print("hello  ".rstrip())        # hello


# ---------------------------
# SPLIT & JOIN METHODS
# ---------------------------

print("a,b,c".split(","))         # ['a', 'b', 'c']
print("a,b,c".rsplit(",", 1))     # ['a,b', 'c']
print(",".join(["a", "b", "c"]))  # a,b,c
print("My name is {}".format("Parthiban"))  # My name is Parthiban
print("hello".encode())           # b'hello'


# ---------------------------
# ALIGNMENT & PADDING
# ---------------------------

print("hi".center(6, "*"))        # **hi**
print("hi".ljust(5, "."))         # hi...
print("hi".rjust(5, "."))         # ...hi
print("42".zfill(5))              # 00042


# --------------
