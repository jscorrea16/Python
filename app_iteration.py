n = 5
while n > 0 :
    print(n)
    n = n - 1
print("Blastoff!")
print(n)
# Loops (repeated steps) have iteration
# variables that change each time through
# a loop. Often these iteration variables
# go through a sequence of numbers.

# An Infinite Loop
# n = 5
# while n > 0 :
    # print("Lather")
    # print("Rinse")
# print("Dry off!")

# Another Loop
n = 0
while n > 0 :
    print("Lather")
    print("Rinse")
print("Dry off!")

# Breaking Out of a Loop
# The break statement end the current
# loop and jumps to the statement
# immediately following the loop.
# It is like a loop test that can happen
# anywhere in the body of the loop.
while True:
    line = input("> ")
    if line == "done" :
        break
    print(line)
print("Done")

# Finishing an Iteration with continue
# The continue statement end the current iteration
# and jumps to the top of the loop and starts
# the next iteration.
while True:
    line = input("> ")
    if line[0] == "#" :
        continue
    if line == "done" :
        break
    print(line)
print("Done!")