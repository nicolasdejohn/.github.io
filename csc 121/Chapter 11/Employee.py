# Nicolas DeJohn | Chapter 11-1 Lab | April 6 2021

'''The purpose of this program is to create an Employee class and a Production Worker subclass.'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 11")

# Initialize the Employee class
class Employee:
    # Defines the function that is run when an instance of the class is called
    def __init__(self, name, number ):
        self.__name = name
        self.__number = number

    # Mutators
    def change_name(self, name):
        self.__name = name

    def change_number(self, number):
        self.__number = number

    # Accessors
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    


class ProductionWorker(Employee):
    # Defines the function that is run when an instance of the class is called
    def __init__(self, name, number, shiftNumber, payRate):
        Employee.__init__(self, name, number)
        # Additional attributes that extend the Employee class
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate
    
    # Mutators
    def change_shiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
    
    def change_payRate(self, payRate):
        self.__payRate = payRate

    # Accessors
    def get_shiftNumber(self):
        return self.__shiftNumber

    def get_payRate(self):
        return self.__payRate