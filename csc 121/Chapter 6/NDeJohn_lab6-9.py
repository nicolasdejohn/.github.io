# Nicolas DeJohn /Chapter 6-9 / January 16th 2021
"""
The purpose of this program is to read numbers from "numbers.txt", 
calculate their total and average, and print the results.

"""
# Defines the main module that calls printOutput() when program is executed.
def main():
    printOutput() # Calls the printOutput()

# Returns the total number of lines read in the document    
def getAmountOfNumbers():
    numbersFile = open("numbers.txt", "r")
    line = numbersFile.readline()     # Initalizes the variable that will store the next read line in memory.
    totalNumbers = 0                  # Initializes the variable that will divide the total sum of numbers to get the average
    while line != '':                 # While the next line does not contain an empty string..
        totalNumbers += 1             # Add 1 to the total of numbers in the document
        line = numbersFile.readline() # Read the next line.
    return totalNumbers               # Returns totalNumbers when the function is called. 
    numbersFile.close()               # Close the file

# Gets the numbers from each line in the document and returns the sum of their values
def calculateTotal(): 
    numbersFile = open("numbers.txt", "r")
    line = numbersFile.readline()     # Initalizes the variable that will store the next read in memory.
    total = 0                         # Initializes the variable that will store the total of all numbers in the file.
    while line != '':                 # While the next line does not contain an empty string..
        total += int(line)            # The number on the current line is added to total
        line = numbersFile.readline();# Read the next line   
    numbersFile.close()               # Close the file
    return total

# Takes the returned sum from calculateTotal() and divides it by the returned value of getAmountOfNumbers()
def calculateAverage():
    # returned value from calculateTotal() divided by returned value from getAmountOfNumbers() 
    average = calculateTotal() / getAmountOfNumbers() 
    return average

# Compiles the returned values from each module into meaningful output while checking for ValueErrors and IOErrors.
def printOutput():
    try: # Checks that numbers.txt exsists
        try: # Checks that each line in the file is a number
            print("Sum of numbers in document: " + str(calculateTotal()))
            print("The average of numbers in document: " + str(calculateAverage()))
        except ValueError: # Prints an error message is any line is not a number
            print("Error! One or more lines in the document are not numbers. Edit the document to contain only numbers.")
        print("Total lines read: " + str(getAmountOfNumbers()))
    except IOError: # Prints an error message is numbers.txt was not found. 
        print("Error! The file 'numbers.txt' was not found!")

main() # Calls the main module when program is executed.