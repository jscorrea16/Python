message = "Hi Joshua."
print(message)

# Dr. Severance from June 26, 2022.
# Free Code Camp.
x = 5
print("Hi")

# This defined function has not been
# called/invoked.
def print_lyrics(): 
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print("Yo")
# The defined function has now
# been called/invoked.
print_lyrics()
x = x + 2
print(x)

# Arguments
big = max("Hello World")
# "Hello World" is the argument.

# Parameters
# A parameter is a variable which
# we use in the function definition.
# It is a "handle" that allows the 
# code in the function to access
# the arguments for a particular
# function invocation.
def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")

greet("en")
greet("es")
greet("fr")

# Return Values
# Often a function will take its
# arguments, do some computation,
# and return a value to be used
# as the value of the function
# call in the calling expression.
# The return keyword is used for this.
def greet():
    return "Hello"

print(greet(), "Glenn.")
print(greet(), "Sally.")

# Multiple Parameters/Arguments
# We can define more thatn one parameter
# in the function definition. We simply
# add more arguments when we call the function.
# We match the number and order of arguments 
# and parameters.
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)