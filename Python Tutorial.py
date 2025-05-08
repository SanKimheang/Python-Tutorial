# First coding
# This is a comment
# Written in
# more than just one line
"""
This is a comment
written in
more than just one line
"""
#print("Hello, World!" )

"""Variables are containers for storing data values.
Variables do not need to be declared with any particular type
and can even change type after they have been set."""
#x = 5
#y = "John"
# print(x)
#print(y)

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)
# print(x + y) # This will cause an error because x is an int and y is a str

# Casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# Get the Type
#x = 5
# y = "John"
# print(type(x)) # <class 'int'>
# print(type(y)) # <class 'str'>
# print(type(3.14)) # <class 'float'>

# Variable Names
# myvar = "Heang"
# my_var = "Heang"
# _my_var = "Heang"
# myVar = "Heang"
# MYVAR = "Heang"
# myvar2 = "Heang"

# Multiple words variable names
# myVariableName = "Heang"
# MyVariableName = "Heang"
# my_variable_name = "Heang"

# Assign Multiple Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# ONe Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Output Variables
# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = " Python"
# y = " is"
# z = " awesome"
# print(x + y + z)

# Glocal Variables
# Global variables can be used by everyone, both inside of functions and outside.
# x = "awesome"
# def myfunc():
#     print("Python is " + x)
# myfucn()

"""If you create a variable with the same name inside a function, this variable will be local,
and can only be used inside that function. The global variable with the same name will remain as it was, global and with the original value."""
# x = "awesome"
# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
# def myfunc():
#     global y
#     y = "beautiful"
# myfunc()
# print("Python is " + y)

# x = " awesome"
# def myfunction():
#     global x
#     x = "beautiful"
# myfunction()
# print("Python is " + x)