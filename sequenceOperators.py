string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "

print(string1+string2+string3+string4+string5)

# But the plus isn't necessary, you can also do

print("He's " "probably " "pining " "for " "the " "fjords ")

# Strings can also be multiplied
print("Hello \n" * 5) # This will print out the string 5 times in new lines

# There's also an operator to check if a string is a substring of another
today = "Friday"
print("day" in today) # will give out the boolean value after checking whether the sequence day is present in Friday
# Here the in operator evaluate whether the first string exists in the other string
# in will be used a lot in for loops

