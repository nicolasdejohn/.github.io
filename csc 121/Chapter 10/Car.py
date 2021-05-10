# Nicolas DeJohn | Chapter 10-2 Lab | April 3 2021

'''The purpose of this program is to create a Car class that can be used to create an instance of a car object'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

# Initialize the class Car
class Car: 

    # The __init__ method sets the data attributes to the parameters when the class is created
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0
    # Accelarate increases the car's speed attribute by 5 each time it's called
    def accelarate(self):
        self.__speed += 5

    # Brake increases the car's speed attribute by 5 each time it's called
    def brake(self):
        self.__speed -= 5
    
    # get_speed returns the current value of the car's speed attribute
    def get_speed(self):
        return self.__speed



