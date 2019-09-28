# Exercise: Find the errors
# File: errors.py
# Purpose: A program with lots of errors
#
# It should end up working like this:
#
#    c:\> python errors.py
#    Enter your name, please: Batman
#    What is your favorite number: 9
#    Batman, the square of 9 is 81!

name = input("Enter your name, please: ")
number = int(input("What is your favorite number: "))
numSquare = number * number
print(name,end='')
print(', the square of', number, 'is', numSquared,end='')
print("!")