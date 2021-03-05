# Nicolas DeJohn | Chapter 8-15 Lab | March 3rd 2021

'''
The purpose of this program is to calculate the average gas prices per year from 1993-2013, calculate the average gas prices per month,
display the highest and lowest prices per year, and generate two text files displaying low to high prices, and high to low prices respectedly.

'''

import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")
cwd = os.getcwd()

file = open("GasPrices.txt", "r") # Opens the file
myList = [] # Initializes this list to store the data in the file.
monthList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] # Initializes this list to keep month in 'XX' format.
currentYear = 1993 # Initialzing the year that the loops will use.


def main():
    for i in file: # Get the data from the file and append it to the list
        myList.append(i.rstrip()) 

    averagePerYear(currentYear)
    averagePerMonth(monthList)
    highLowPerYear(currentYear)
    sortMyListLow()
    sortMyListHigh()
    print("\n'Low to High.txt' and 'High to Low.txt' have been created in '" + cwd + "'\n")
    file.close()

def averagePerYear(currentYear): # Function that averages the price per year.
    print("\nAverage gas prices per year: \n") # Nice title..
    while currentYear < 2014: 
        divisor = 0 # Initializes a divisor for calculating the average
        addedPrice = 0 # adds the float to addedPrice
        for i in myList: 
            if str(currentYear) in i[6:10]: # Checks if the current year is in the 6th through 10th string index of 'i'. 
                price = float(i[11:]) # Sets the 11th index of i to a float for calculation
                addedPrice += price 
                divisor += 1 
        averagePrice = addedPrice / divisor # Calculate the average 
        print("\t" + str(currentYear) + " - $" + str(format(averagePrice, '.3f'))) # Print results
        currentYear += 1 # add 1 to the current year

def averagePerMonth(monthList): # Function that averages the price per month.
    print("\nAverage gas prices per month:\n") 
    monthListIndex = 0 # Initializes the index for monthList
    while monthListIndex != 12: # Checks to make sure the index doesn't exceed 12 months..
        divisor = 0 # Initializes a divisor for calculating the average
        addedPrice = 0 # adds the float to addedPrice
        for i in myList: # Loop through myList
            if monthList[monthListIndex] in i[:2]: # Checks if the current monthList index is in the string of current index of myList
                price = float(i[11:]) # Sets the 11th index of i to a float for calculation
                addedPrice += price # adds the float to addedPrice
                divisor += 1 # add to divisor
        averagePrice = addedPrice / divisor # Calculate the average and store it in averagePrice
        print("\t" + str(monthList[monthListIndex]) + " - $" + str(format(averagePrice, '.3f'))) # Print results
        monthListIndex += 1 # Increases the index of monthList for the next loop..

def highLowPerYear(currentYear): # Function that displays the high's and low's of all years.
    print("\nHighest and lowest prices per year: \n") # Nice title..
    minMaxList = [] # Initializes an empty list to store all the prices per year
    while currentYear < 2014: # Checks to make sure current year doesn't exceed 2014..
        for i in myList: # Loop through myList
            if str(currentYear) in i[6:10]: # Checks if the current year is in the indexes 6th through 10th index of the string
                minMaxList.append(float(i[11:])) # append each price for that year to the list
        print(str(currentYear) + ":\n\t High: $" + str(max(minMaxList)) + "\n\t Low: $" + str(min(minMaxList))) # prints year, and the max and min in the current version of the array
        minMaxList.clear() # resets the array
        currentYear += 1 # adds 1 to the current year

def sortMyListLow(): # Function that creates a file of gas prices sorted from lowest to highest.
    def getEleventhIndex(elem):
        return elem[11:]
    file = open("Low to High.txt" , "w") # Opens or creates a new file for writing
    myList.sort(key=getEleventhIndex) # Sorts the list in ascending order
    for i in myList: # Loops through the list..
        file.write(i[0:11] + " $" + i[11:] + "\n") # Writes each index onto a new line in the file with a little formatting flare.

def sortMyListHigh(): # Function that creates a file of gas prices sorted from highest to lowest.
    def getEleventhIndex(elem): # Function that returns the 11th string index of each index in myList.
        return elem[11:]
    file = open("High to Low.txt" , "w") # Opens or creates a new file for writing
    myList.sort(key=getEleventhIndex, reverse=True) # Sorts the list in descending order
    for i in myList: # Loops through the list..
        file.write(i[0:11] + " $" + i[11:] + "\n") # Writes each index onto a new line in the file with a little formatting flare.

main() # Ta-daaaaa



