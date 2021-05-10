# Nicolas DeJohn | Chapter 10-3 Lab | April 3 2021

'''The purpose of this program is to take a user's personal information and set it to the class's data attributes'''
#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

# import PersonalInfo.py
import PersonalInfo

# Call the two functions
def main():
    userInfo()
    familyFriendInfo()
    familyFriendInfo()

# Initializes the Info class with the user's personal information
def userInfo():
    userName = str(input("Enter your name: "))
    userAddress = str(input("Enter your address "))
    userAge = str(input("Enter your age: "))
    userPhone = str(input("Enter your phone number "))

    # Create an instance of the object with the variables as arguments
    userInfo = PersonalInfo.Info(userName, userAddress, userAge, userPhone)

    # Display the information
    print()
    print(userInfo)
    print()

# Initializes the Info class with the user's family/friend personal information
def familyFriendInfo():
    userName = str(input("Enter your family/friend name: "))
    userAddress = str(input("Enter your family/friend address "))
    userAge = str(input("Enter your family/friend age: "))
    userPhone = str(input("Enter your family/friend phone number "))

    # Create an instance of the object with the variables as arguments
    userInfo = PersonalInfo.Info(userName, userAddress, userAge, userPhone)

    # Display the information
    print()
    print(userInfo)
    print()

# Call the main function
main()

