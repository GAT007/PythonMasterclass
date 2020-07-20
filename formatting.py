for i in range(1,13) :
     print ("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# You can give any expressions you want in the format parentheses. It doesn't have to be just numbers or strings

# The main thing to focus on here is the formatting, if you don't give any additional parameters
# the for loop will print it out as it is written in the print command
# which will result in generally untidy printing
# Adding a colon followed by a number after the format parameter as seen above will result
# in it being displayed more neatly (Format {0:2})

print()

# You can also left align or right align values, by adding a lesser than or greater than symbol before the formatting number
# You can also center it by using the carat symbol
for i in range(1,13) :
    print ("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Base code general format
print("Pi is approximately {0:12}".format(22/7))
# Using float point format default of 6 digits
print("Pi is approximately {0:12f}".format(22/7))
# Using precision float, if precision float is greater than the value column width specified, precision value is printed
print("Pi is approximately {0:12.50f}".format(22/7))
# Using precision float, the next three are to make it evident
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
