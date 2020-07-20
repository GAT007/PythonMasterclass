# Strings are a datatype of sequence

#         012345678901234
parrot = "Norwegian blue"
print(parrot)
print(parrot[3])

# Mini Challenge
# Add some code to the program, so that it prints out the line "we win"
# Each character should appear on a separate line
# The program should get the characters from the parrot string, using indexing
# The w is already printed out, so you just need 5 more characters

print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# Mini challenge 2
# Use negative indexing to print out the same message

print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print()

# Slicing
# You need to provide three integer values in the function parameter block
# They are the start, stop and strip values

# Slicing without strip
print(parrot[0:6]) # Norweg
print(parrot[0:9])

# You can also leave off the start value if your start position is zero
print(parrot[:9])

# But if you want from a specific point, you gotta specify it
print(parrot[10:14])

# But if you need the string till the end, then you can leave out the stop value
print(parrot[10:])

# If you fail to mention both the start and stop value, the entire string is printed out
print(parrot[:])

# Slicing with negative numbers
# You can slice with negative numbers but you have to make sure that the indices are right
print(parrot[-4:13])

# Using a step in a slice means to step over so many characters in the string
print(parrot[0:8:2]) # will print out Nrei where it begins printing from 0 and prints out characters at positions 0,2,6 and 8
print(parrot[1:9:2]) # will print out owga where it begins from 1 and prints out the characters at positions 1,3,5 and 7

number = "9,223;372:036 854,775;807"
print(number[1::4])

# using separators
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
