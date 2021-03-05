# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021

'''
The purpose of this program is to ask the user to enter a phone number that has 
alphabetic characters, and convert them into a numeric phone number.

'''

import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")


file = open("GasPrices.txt", "r")
myList = []
currentYear = 1993

for i in file:
    myList.append(i.rstrip())

print("Average gas prices per year:")

while currentYear < 2014:

    count = 0
    addedPrice = 0
    averagePrice = 0

    for i in myList:
        if str(currentYear) in i:
            price = float(i[11:])
            addedPrice += price
            count += 1

    averagePrice = addedPrice / count
    print("\t" + str(currentYear) + " - $" + str(format(averagePrice, '.3f')))
    currentYear += 1
  