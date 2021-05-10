# Nicolas DeJohn | Chapter 11-3 Lab | April 6 2021

'''The purpose of this program is to create a Person class and a Customer subclass.'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 11")

# Define the Person Class
class Person:
    # Defines the function that is run when an instance of the class is called
    def __init__(self, name, address, phoneNumber):
        self.__name = name
        self.__address = address
        self.__phoneNumber = phoneNumber

    # Mutators
    def change_name(self, name):
        self.__name = name

    def change_address(self, address):
        self.__address = address

    def change_phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    # Accessors
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phoneNumber(self):
        return self.__phoneNumber

# Define the Customer subclass  
class Customer(Person):
    # Defines the function that is run when an instance of the class is called
    def __init__(self, name, address, phoneNumber, customerNumber, onMailingList):
        Person.__init__(self, name, address, phoneNumber)
        # Additional attributes that extend the Employee class
        self.__customerNumber = customerNumber
        self.__onMailingList = onMailingList

    # Mutators
    def change_customerNumber(self, customerNumber):
        self.__customerNumber = customerNumber
    
    def change_onMailingList(self, onMailingList):
        self.__onMailingList = onMailingList

    # Accessors
    def get_customerNumber(self):
        return self.__customerNumber

    def get_onMailingList(self):
        return self.__onMailingList