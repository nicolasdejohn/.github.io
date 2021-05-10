# Nicolas DeJohn | Chapter 9-5 Lab | March 26 2021

'''
The purpose of this program to read a file and store the number of occurances for each word in a dictionary.

'''

import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 9")

# Defines main function
def main():
    # Opens and reads the file
    file = open("text95.txt", "r")
    readFile = file.read()
    file.close()

    dictionary = {} # Initializes an empty dictionary
    unwantedChars = ".,_-()!?'" # Establishes characters that will be removed
    words = readFile.split() # Creates an array of every word without spaces

    # Loop through the words array
    for i in words:
        words = i.strip(unwantedChars) # Remove unwanted characters
        if words not in dictionary: # If the key doesn't exist..
            dictionary[words] = 0
        dictionary[words] += 1 # Add 1 to the key's value

    print(dictionary) # Display information
    
# Call the main function
main() 
