# Nicolas DeJohn | Chapter 10-3 Lab | April 3 2021

'''The purpose of this program is to create a class Info that stores a user's personal information.'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

#Initialize the class
class Info:

    # Initialize the data attributes of this class
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # get_name returns the name attribue of this class
    def get_name(self):
        return self.__name
    # get_address returns the address attribue of this class
    def get_address(self):
        return self.__address
    # get_age returns the age attribue of this class
    def get_age(self):
        return self.__age
    # get_phone returns the phone attribue of this class
    def get_phone(self):
        return self.__phone
    # __str__ returns the state of this object
    def __str__(self):
        return "Name: " + self.__name + "\n" +"Adress: " + self.__address + "\n" + "Age: " + self.__age + "\n" + "Phone: " + self.__phone