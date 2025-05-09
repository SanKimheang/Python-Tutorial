# First coding
# This is a comment
# Written in
# more than just one line
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!" )

"""Variables are containers for storing data values.
Variables do not need to be declared with any particular type
and can even change type after they have been set."""
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
print(x + y) # This will cause an error because x is an int and y is a str

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
x = 5
y = "John"
print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(3.14)) # <class 'float'>

# Variable Names
myvar = "Heang"
my_var = "Heang"
_my_var = "Heang"
myVar = "Heang"
MYVAR = "Heang"
myvar2 = "Heang"

# Multiple words variable names
myVariableName = "Heang"
MyVariableName = "Heang"
my_variable_name = "Heang"

# Assign Multiple Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# ONe Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = " Python"
y = " is"
z = " awesome"
print(x + y + z)

# Glocal Variables
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

"""If you create a variable with the same name inside a function, this variable will be local,
and can only be used inside that function. The global variable with the same name will remain as it was, global and with the original value."""
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global y
    y = "beautiful"
myfunc()
print("Python is " + y)

x = " awesome"
def myfunction():
    global x
    x = "beautiful"
myfunction()
print("Python is " + x)

# Built-in Data Types
"""
 Text Type:	str
 Numeric Types:    int, float, complex
 Sequence Types:	list, tuple, range
 Mapping Type:	dict
 Set Types:	set, frozenset
 Boolean Type:	bool
 Binary Types:	bytes, bytearray, memoryview
 None Type:	NoneType
"""
x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name": "John", "age": 36} # dict
x = {"apple", "banana", "cherry"} # set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview
x = None # NoneType

# Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Intergers
x = 1
y = 35656222554887711
z = -3255522

# Float
x = 1.10
y = 1.0
z = -35.59

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3 # 35 * 10^3
y = 12E4 # 12 * 10^4
z = -87.7e100 # -87.7 * 10^100

# Complex Numbers
x = 3 + 5j
y = 5j
z = -5j

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

# Random Number
import random
print(random.randrange(1, 10)) # Return a random number between 1 and 10
print(random.randint(1, 10)) # Return a random number between 1 and 10, including 10
print(random.random()) # Return a random float number between 0.0 to 1.0
print(random.choice([1, 2, 3, 4, 5])) # Return a random element from the list
print(random.uniform(1, 10)) # Return a random float number between 1 and 10

# Python Casting
# intergers
x = int(1)    # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
# floats
x = float(1)    # x will be 1.0
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
w = float("4.2") # w will be 4.2
# strings
x = str(1)    # x will be '1'
y = str(2)    # y will be '2'
z = str(3.0)    # z will be '3.0'

# Python Strings
print("Hello")
print('Hello')
print(" It's alright")
print('He said "Hello"')
print('He is called "Kimheang"')

# assign a string to a variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(a)
# or
a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1]) # e
print(a[0]) # H

# Looping Through a String
for x in "banana":
    print(x)

# String Length
a = "Hello, World!"
print(len(a)) # 13

# Check String
txt = "The best things in life are free!"
print("free" in txt) # True
# or
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
txt = "I love Swimming!"
print(" swimming" not in txt)
# or
txt = "I love Swimming!"
if "swimming" not in txt:
    print("No, 'swimming' is NOT present.")

# Python - Slicing Strings
# Slicing is done by specifying a start and end index
b = "Hello, World!"
print(b[2:5]) # llo
print(b[:5]) # Hello
print(b[2:]) # llo, World!
# Negative Indexing
print(b[-5:-2]) #orl

# Python - Modify Strings
# Upper Case
a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!
# Lower Case
a = "Hello, World!"
print(a.lower()) # hello, world!
# Remove Whitespace
a = "   Hello, World!   "
print(a.strip()) # Hello, World!
# Replace String
print(a.replace("H", "J")) # Jello, World!
# Split String
print(a.split(",")) # ['Hello', 'World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c) # Hello World

# String Format
"""
age = 36
txt = "My name is John, and I am " + age
print(txt)   This will cause an error
"""
# F-Strings
age = 22
txt = f"My name is Heang , I am {age}"
print(txt) # My name is Heang , I am 22
# Placeholders
price = 69
txt = f"The price is {price} dollars"
print(txt)
# Display the price with 2 decimals
txt = f"The price is {price:.2f} dollars"
print(txt) # The price is 69.00 dollars
# A placeholder can contain Python code, like math operations:
txt = f"The price is {price + 10} dollars"
print(txt) # The price is 79 dollars

# Escape Characters
"""
txt = "We are the so-called "Vikings" from the north."
print(txt)   This will cause an error
"""
# To fix this problem, we can use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."
print(txt) # We are the so-called "Vikings" from the north.

# String Methods
"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

# Python Booleans
# A boolean value is one of two constant values: True or False.
print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False
# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
print(bool("Hello")) # True
print(bool(15)) # True
# Most values are evaluated to True.
bool("abc") # True
bool(123) # True
bool(["apple", "banana", "cherry"]) # True
# Some values are evaluated to False.
bool(False) # False
bool(None) # False
bool(0) # False
bool("") # False
bool(() ) # False
bool([]) # False
bool({}) # False
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj)) # False
# Functions can return a boolean Value
def myFunction():
    return True
print(myFunction()) # True
# Print "YES!" if the variable a is True
def myFunction():
    return True
if myFunction():
    print("YES!") # YES!
else:
    print("NO!")
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int)) # True

# Python Operators
print(10 + 5) # Addition
print(10 - 5) # Subtraction
print(10 * 5) # Multiplication
print(10 / 5) # Division
print(10 % 5) # Modulus
print(10 ** 5) # Exponentiation
print(10 // 5) # Floor division
# Assignment Operators
x = 5
x += 3 # x = x + 3
print(x) # 8
x -= 3 # x = x - 3
print(x) # 5
x *= 3 # x = x * 3
print(x) # 15
x /= 3 # x = x / 3 
print(x) # 5.0
x //= 3 # x = x // 3
print(x) # 1.0
x %= 3 # x = x % 3
print(x) # 1.0
x **= 3 # x = x ** 3
print(x) # 1.0
x &= 3 # x = x & 3
print(x) # 1.0
x |= 3 # x = x | 3
print(x) # 3.0
x ^= 3 # x = x ^ 3
print(x) # 0.0
x >>= 3 # x = x >> 3
print(x) # 0.0
x <<= 3 # x = x << 3
print(x) # 0.0
# Comparison Operators
x = 5
y = 10 
print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True
# Logical Operators
x = True
y = False
print(x and y) # False
print(x or y) # True
print(not x) # False
# Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y) # False
print(x is z) # True
print(x is not y) # True
print(x is not z) # False
# Membership Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
print("banana" in x) # True
print("banana" not in x) # False
# Bitwise Operators
x = 5
y = 3
print(x & y) # 1
print(x | y) # 7
print(x ^ y) # 6
print(x << y) # 40
print(x >> y) # 0
# Operators Precedence
print((6 + 3) - (2 * 5)) # 1
print(6 + 3 - 2 * 5) # 1

# Python Lists
# A list is a collection which is ordered and changeable. Allows duplicate members.
thislist = ["apple", "banana", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry']
# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print (thislist)
# List Length
print(len(thislist))
# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 4, 5, 8]
list3 = [True, False, False]
# A list can contain different data types:
list = ["abc", 34, True, 22, 45.67, "male"]
# Type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# Access List Items
print(thislist[1]) # banana
# Negative Indexing
# -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1]) # cherry
# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[2:5]) # ['cherry', 'orange', 'kiwi']
print(thislist[:4]) # ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:]) # ['cherry', 'orange', 'kiwi', 'mango']
print(thislist[-4:-1]) # ['orange', 'kiwi', 'mango']
# Check if Item Exists
list = ["apple", "banana", "cherry"]
if "apple" in list:
    print("Yes, 'apple' is in the fruits list")
# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry']
# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']
# Change the second and third value by replacing it with one new value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # ['apple', 'watermelon']
# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']

# Add List Items
# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'cherry', 'orange']
# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# Remove List Items
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']
# If there are more than one item with the specified value, the remove() method removes the first occurrence of the value.
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry', 'banana']
# Remove Specified Index
# The pop() method removes the specified index, (or the last item if index is not specified)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # ['apple', 'cherry']
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ['apple', 'banana']
# Delete List Items
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # ['banana', 'cherry']
# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
# Clear the List
thislist.clear()
print(thislist)