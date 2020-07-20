print("Today is a good day to learn Python!")
print('Python is fun!')
print('Python\'s string are easy to use')
print('We can even include "quotes" in strings')
print("Hello " + "World!")
greeting = "Hello "
name = "Amith "

# if you want a space you can add that too
print(greeting+' '+name)

# to make this more useful you can even accept inputs
# name = input("Please enter your name")
print(greeting+name)


# Dealing with variables
age = 24
print(age)

# Python can tell you the name of the type being supplied to the arguments
print(type(age))
print(type(greeting))

# What does python is a dynamically typed language?
# Here, greeting and name are strings and age is an int
# But in python variable types are checked during run time and not compile time
# So, you can reassign variable names without having to consider what type is being supplied
# For example

age_in_words = "2 years"
print("Age is of type string now " + age_in_words)
print(type(age))

# But this doesn't mean python is a weakly typed language
# Let's see what happens when you try to concatenate a string and an int value

print(name + " is " + age_in_words + " old")

# So, the error message tells us that it is a type error.
# Which means that you gave two different types and tried to combine them

# Using f-strings
# Available only if you are using Python 3.6 and above
# You can use this just by adding an f before the string you want to print and putting the variable name in curly parentheses

print(name + f"is {age} old")

print(f"Pi is approximately {22/7:12.50f}")



