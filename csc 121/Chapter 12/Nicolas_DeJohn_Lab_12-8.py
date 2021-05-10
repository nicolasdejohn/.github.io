# Nicolas DeJohn | Chapter 12-8 Lab | April 18 2021

'''
The purpose of this program is to display Ackermanns Function that accepts two arguments. 

'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 9")

# Define Ackermann
def ackermann(m, n): 
    if m == 0:
        print(m, n)
        return n + 1
    elif n == 0: # if m > 0 and n = 0
	    print(m, n) # Print the next numbers
	    return ackermann(m-1, 1)
    else: 
	    print(m, n) # Print the next numbers
	    return ackermann(m-1, ackermann(m, n-1))

# Define the main function
def main():
    m = int(input("Enter first integer: "))
    n = int(input("Enter second integer: "))

    # Print the ackermann function
    print(ackermann(m, n)) 
    
# Call the main function
main()