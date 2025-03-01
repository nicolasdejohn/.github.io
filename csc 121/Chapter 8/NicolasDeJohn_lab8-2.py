# Nicolas DeJohn | Chapter 8-2 Lab | March 1st 2021
""" 
The purpose of this program is to prompt the user for a series of numbers with no spaces or special characters, and totaling up those numbers together.
"""

"""Using this as fail-safe to get my python programs to work.."""
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")

stringOfNumbers = str(input("Enter a series of numbers with no spaces or special characters: ")) # Gets the users string of numbers.
total = 0 # initiates the total variable.

for ch in stringOfNumbers.replace(" ", ""): # Iterate over each index of the string. I used the replace method in case the space key was pressed during input.
    total += int(ch) # adds the current index of the string (converted to an integer) to the total variable.


print("Sum of the digits: " + str(total)) # prints the total.
