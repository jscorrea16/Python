# String Data Type
# A string is a sequence of characters.
# A string literal uses quotes 'Hello' or "Hello".
# For strings, + means "concatenate"
# When a string contains numbers, it is still a string.
# We can convert numbers in a string into a number using int().

# Reading and Converting
# We prefer to read data using strings and then parse and convert
# the data as we need.
# This gives us more control over error situations and/or bad user input.
# Raw input numbers must be converted from strings.

# Looking Inside Strings
# We can get at any single character in a string using an index specified
# in square brackets [].
# The index value must be an integer and starts at zero.
# The index value can be an expression that is computed.

fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# A Character Too Far
# You will get a python error if you attempt to index
# beyond the end of a string.
# So be careful when constructing index values and slices.

# Strings Have Length
# The built-in len gives us the length of a string.

fruit = 'banana'
print(len(fruit))

# Len Function
# A function is some stored code that we use. A funciton
# takes some input and produces an output.

fruit = 'banana'
x = len(fruit)
print(x)

# Looping Through Strings
# Using a while statement and an iteration variable, and 
# the len function, we can construct a loop to look at each
# of the letters in a string individually.

fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Looping Through Strings (2)
# A definite loop using a for statement is much more elegant.
# The iteration variable is completely taken care of by the for loop.

fruit = 'banana'
for letter in fruit :
    print(letter)

# Looping and Counting
# This is a simple loop that loops through each letter in a 
# string and counts the number of times the loop encounters
# the 'a' character.

word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)

# Looking Deeper Into 'in'
# The iteration variable 'iterates through the sequence
# (ordered set).
# The block (body) of code is executed once for each value
# in the sequence.
# The iteration variable moves through all of the values 
# 'in' the sequence.