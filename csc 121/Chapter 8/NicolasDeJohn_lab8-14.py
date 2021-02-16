# Nicolas DeJohn | Chapter 7-2 Lab | January 24th 2021

'''
The purpose of this program is to ask the user to enter a phone number that has 
alphabetic characters, and convert them into a numeric phone number.

'''
import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")

file = open("pbnumbers.txt", "r")
myList = []

previousValue = ""
winningSets = []

generalNumbers = []
powerballNumbers = []

for i in file:
    myList = myList + i.split()
    winningSets.append(i.split())
    generalNumbers = generalNumbers + i.split()[0:5]
    powerballNumbers = powerballNumbers + i.split()[5:]



print(collections.Counter(myList).most_common(10))
print(collections.Counter(myList).most_common()[:-10-1:-1])
print(collections.Counter(generalNumbers).most_common())
print(collections.Counter(powerballNumbers).most_common())




