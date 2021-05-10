# Nicolas DeJohn | Chapter 12-2 Lab | April 18 2021

'''
The purpose of this program is to take two numbers and multiply them through a recursive function. 

'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 9")

# Define the recursive function
def multiply(x, y):
    if x == 1:
        return y # Return Y
    else:
        return y + multiply(x - 1, y) # Continuously adds Y until X equals 1

# Define the main function
def main():
    # Get two numbers
    x = int (input ("Enter the first number: "))
    y = int (input ("Enter the second number: "))
    # Print the result
    print (x, "x", y, "=", multiply(x, y))

# Call the main function
main()