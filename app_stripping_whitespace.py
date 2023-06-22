# Slicing Strings
# We can also look at any continuous section
# of a string using a colon operator.
# The second number is one beyond the end of the slice
# 'up to but not including'
# If the second number is beyond the end of the string,
# it stops at the end.

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# Slicing Strings (2)
# If we leave off the first number or the last number
# of the slice, it is assumed to be the beginning or
# end of the string respectively.

s = 'Monty Python'
print(s[:2])
print(s[8:])
print(s[:])

# String Concatenation
# When the + operator is applied to strings,
# it means 'concatenation'.

a = 'Hello'
b = a + 'There'
print(b)

c = a + ' ' + 'There'
print(c)

# Using 'in' as a logical Operator
# The 'in' keyword can also be used to check to see
# if one string is 'in' another string.
# The 'in' expression is a logical expression that
# returns True or False and can be used in an if
# statement.

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
    print('Found it!')

# String Comparison

word = 'banana'
if word == 'banana':
    print('All right, bananas')

if word < 'banana':
    print('Your word,' + word + ', come before banana.')
elif word > 'banana':
    print('Your word,' + word + ', come after banana.')
else:
    print('All right, bananas.')

# String Library
# Python has a number of string funcitons
# which are in the string library.
# These functions are already built into every string
# we invoke them by appending the funtion to the string
# variable.
# These functions do not modify the original string,
# instead they return a new string that has been altered.

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

# Searching a String
# We use the find() function to search
# a substring within another string.
# Find() finds the first occurrence of the
# substring.
# If the substring is not found, find()
# returns -1.
# Remember that string position starts at zero.

fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('x')
print(aa)

# Making everythin UPPER CASE
# You can make a copy of a string
# in lower case or upper case.
# Often when we are searching for
# a string using find() we first
# convert the string to lower case
# so we can search a string regardless
# of case.

greet = 'Hello Joshua'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

# Search and Replace
# The replace() funciton is like
# a "search and replace" operation
# in a word processor.
# It replace all occurrences of the search
# string with replacement string.

greet = 'Hello Michelle'
nstr = greet.replace('Michelle', 'Gaudia')
print(nstr)
nstr = greet.replace('e', 'A')
print(nstr)

# Stripping Whitespace
# Sometimes we want to take a string
# and remove whitespace at the beginning
# and/or end.
# Istrip() and rstrip() remove whitespace
# at the left or right.
# strip() removes both beginning and
# ending whitespace.

greet = '  Hello Chris  '
left = greet.lstrip()
print(left)
right = greet.rstrip()
print(right)
both = greet.strip()
print(both)

# Prefixes

line = 'Please have a nice day'
prefix = line.startswith('Please')
print(prefix)
prefixes = line.startswith('p')
print(prefixes)

# Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)