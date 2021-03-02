# Nicolas DeJohn | Chapter 8-2 Lab | March 1st 2021
""" 
The purpose of this program is to open stringONumbers.txt for reading, get the numbers listed as a string, and use a loop 
to get the sum of all the numbers in the string.
"""

"""Still using this fail-safe to get my python programs to work.."""
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")

stringOfNumbers = str(input("Enter a series of numbers with no spaces or special characters: ")) # Gets the users string of numbers.
total = 0 # initiates the total variable.

for ch in stringOfNumbers: # iterate over each index of the string
    total += int(ch) # adds the current index of the string (converted to an integer) to the total variable.


print("Sum of the digits: " + str(total)) # prints the total.
