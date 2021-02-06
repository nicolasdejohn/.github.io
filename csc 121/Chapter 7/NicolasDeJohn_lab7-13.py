# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021
""" 
The purpose of this program is to ask the user to ask the magic 8-ball a question and the ball
will print out an answer from a list that was appended from 8_ball_responses.txt.
"""
#import os
#os.chdir(r"C:\Users\Nick\Desktop\CSC 121\Chapter 7")
import random # Imports the random module for generating random integers.

def main(): # Defines the main function.

    userInput = str(input("Ask the Magic 8-Ball a question! ")) # Gets a question from the user.

    file = open('8_ball_responses.txt' , 'r', encoding='utf-8-sig') # Opens 8_ball_responses.txt for reading.
    # This was interesting. I had to look up the answer to this. Python was not parsing my apostrophe's correctly. The enconding was not UTF-8.

    responseList = [] # Initializes the list that will store the responses

    for i in file: # Loop through the file.
        responseList.append(i.strip()) # Append the current responses that 'i' is at, stripping its new line character.

    response = random.randint(0, 14) # Initializes a variable that stores a random number that will be used as the index in the list.

    print(responseList[response]) # Print the response.

main()

while True: # Loop that allows the user to keep asking questions
    answer = input("Run again? (y/n): ").lower() # Get user input
    if answer not in ('y', 'n'): # If input doesn't equal 'y' or 'n'...
        print("Invalid input.") # ...print this.
        break # Break loop.
    if answer == 'y': # If answer does equal 'y'...
        main() # ...call the main function again.
    else:
        print("Goodbye") # Print this.
        break # Break loop.