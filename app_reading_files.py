# File Processing - A text file can be thought of 
# as a sequence of lines.

# Opening a File
# Before we can read the contents of the file, we must tell Python
# which file we are going to work with and what we will be doing
# with the file.

# This is done with the open() function.
# open() returns a "file handle" - a variable used to perform
# operations on the file. This is similar to "File -> Open" in
# a Word Processor.

# Using open()
# handle = open(filename, mode)
# returns a handle use to manipulate the file
# filename is a string
# mode is optional and should be "r" if we are planning to read the 
# file and "w" if we are going ot write to the file.

# What is a Handle?
# fhand = open('mbox.txt')
# print(fhand)

# The newline Character
stuff = "Hello\nWorld!"
print(stuff)

stuff = "X\nY"
len(stuff)
print(stuff)