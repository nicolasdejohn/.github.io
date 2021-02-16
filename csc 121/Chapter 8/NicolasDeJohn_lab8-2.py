# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021
""" 
The purpose of this program is to open stringONumbers.txt for reading, get the numbers listed as a string, and use a loop 
to get the sum of all the numbers in the string.
"""

"""Still using this fail-safe to get my python programs to work.."""
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")

file = open("stringONumbers.txt", "r") # opens the file for reading
fileString = file.read() # reads the file and adds it as a string to fileString
total = 0 # initiates the total variable

for ch in fileString: # iterate over each index of the string
    total += int(ch) # adds the current index of the string (converted to an integer) to the total variable


print("Sum of the digits listed in this file: " + str(total)) # prints the total
