letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

# Or you can just use
backwards = letters[::-1]
print(backwards)

# but never use -1 cause then you will be requesting a value from a string that starts at z and ends with z
# The letters[::-1] is known as an idiom

# Mini challenge
# Using the letters string from above, create a slice that says qpo
print(letters[16:13:-1])

# Slice the string to produce edcba
print(letters[4::-1])

# Slice the string to produce the last 8 characters, in reverse order
print(letters[26:17:-1])  # zyxwvuts

# Some common python idioms
# to print the last n characters in a sequence
print(letters[-4:])
print(letters[-1:])

# to print the first n characters in a sequence
print(letters[:1])
