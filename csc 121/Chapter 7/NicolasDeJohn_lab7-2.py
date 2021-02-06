# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021
""" 
The purpose of this program is to ask the user how many iterations of winning lottery numbers
they want to generate, and generate 5 numbers, 1 Python Ball number, and a Multiplier Ball
number for each iteration. 
"""
import random # Imports the random module to generate random numbers.

def main(): # Defines the main function.
    
    for i in range(0, userInput()): # Iterates as many times as the user specifies.
        printNumbers(generateWinningNumbers()) # call printNumbers() that prints the returning value from generateWinningNumbers().
    
def userInput():
    # Checks to make sure the user enters a positive integer. 
    while True: # Initializes a generic loop.
        try: # Try checking the input to an integer
            count = int(input("Enter how many sets of winning numbers you want to generate: ")) 
            if count <= 0: # Checks if the input is a negative number.
                print("Use only positive integers.") # Prompts user to use only positive integers.
            else:
                return count
                break # Break the loop if it returns a positve integer.
        except ValueError: # When the exception is raised...
            print("Enter only an integer.") # Output if user input is NOT an integer.

def generateWinningNumbers(): # Generates 5 winning numbers plus the python ball and multiplier.
    
    lotteryNumbers = [] # Initializes the list to be popluated with random numbers.
    
    #Number Ball handler
    for i in range(0, 5): # Iterates 5 times for the first 5 numbers.
        numberBall = random.randint(1, 69) # Initializes the variable for the first 5 numbers.
        while numberBall in lotteryNumbers: # Checks the if the current random number already exists in the list.
            numberBall = random.randint(1, 69) # Generate a new number if the number is in the list.
        lotteryNumbers.append(numberBall) # Add the new random number to the end of the list if it doesn't exist.
    
    #Python Ball handler
    pythonBall = random.randint(1, 69) # Initializes the variable for the python ball.    
    lotteryNumbers.append(pythonBall) # Add the pythonBall random number to the end of the list.

    #Multiplier Ball handler
    multiplierBall = random.randint(1, 5) # Initializes the variable for the multiplier ball.
    lotteryNumbers.append(multiplierBall) # Add the multiplierBall random number to the end of the list.

    return lotteryNumbers # Return this iteration of the populated list.

def printNumbers(numbers): # The print numbers function handles the output with the parameter 'numbers'.

    print("winning numbers: " +  # Concatenated string that lists the indexes separately for presentation. 
        str(numbers[0]) + ", " + 
        str(numbers[1]) + ", " + 
        str(numbers[2]) + ", " + 
        str(numbers[3]) + ", " + 
        str(numbers[4]) + " Python Ball: " + 
        str(numbers[5]) + " Multiplier: " + 
        str(numbers[6])) 

main() # Calls the main() function. 



