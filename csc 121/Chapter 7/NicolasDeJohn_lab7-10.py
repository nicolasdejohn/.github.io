# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021
""" 
The purpose of this program is to ask the user for a baseball team and checks if what year
they won a world series, if any.
"""
'''I was having issues with the directory on my windows machine and it wasn't finding the file so I used 
import os and the method as a quick-fix so I can get this assignment done.
'''
#import os
#os.chdir(r"C:\Users\Nick\Desktop\CSC 121\Chapter 7")

def main(): # Defines the main function.
    userInput = input("Enter name of team: ") # Gets team name from user

    file = open('WorldSeriesWinners.txt' , 'r') # Opens WorldSeriesWinners.txt for reading

    winnerList = [] # Initializes a list for all of the winners.
    yearList = [] # Initializes a list for the years.
    year = 1903 # Initializes the starting year.
    currentYearIndex = 0 # I'm using these variables so that the loops can keep track of both indexes at the same time.
    currentWinnerIndex = 0 # Same as above. This is the second index I'm tracking.
    notInList = True # Initializes a bool in the event the team is not in the list.

    for i in file: # Loop through the file.
        winnerList.append(i.strip()) # Append the current team that 'i' is at, stripping its new line character

    for i in range(0, len(winnerList)): # Loop for the length of winners list.
        yearList.append(year) # Append the current value of year to yearList.
        year += 1 # Add one year to the variable.

    for i in winnerList: # Loop through winnersList
        if userInput.title() == winnerList[currentWinnerIndex]: # If users input, capitalized with .title(), equals the current index..
            print(str(yearList[currentYearIndex]) + ' - ' + str(winnerList[currentWinnerIndex])) # Print the winners index and years index
            notInList = False # notInList must be false
        currentWinnerIndex += 1 # Both indexes are added simultaneously.
        currentYearIndex += 1 # Same as above.

    if notInList == True: # If the team wasn't found..
        print("Team not in list.") # ...print this. 

again = "Y" # Initialzes the variable for the loop.
while again == "Y" or again == "y": # Check if user typed Y or y.
    main() # Run the main function.
    again = input("Would you like to enter another team? Y/N: ") # Ask the user if they want to look up another team.
print("Thanks for using the World Series Winners Index!") # If N, print this. 

