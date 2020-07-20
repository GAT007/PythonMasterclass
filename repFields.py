age = 24
print("My age is " + str(age) + " years")

# This can also be written as follows in Python 3
print("My age is {0} years".format(age)) # Here the replacement field is represented by {} which is then replaced by the first parameter

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "July", "August", "October", "December"))

# Of course, you won't use strings in format, you would probably write it like so
print("There are {0} days in Jan, Mar, May, July, August, October and December".format(31))

# The value that is displayed in the string depends on the index that you use
print("Jan : {2}, Feb : {0}, Mar : {2}, Apr : {1}, May : {2}, Jun : {1}, Jul : {2}, Sep : {1}, Oct : {2}, Nov : {1}, December : {2}".format(28,30,31))

# Obviously if you miss out a value in format it's going to result in an error being thrown

