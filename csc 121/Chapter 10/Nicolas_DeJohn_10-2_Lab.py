# Nicolas DeJohn | Chapter 10-2 Lab | April 3 2021

'''The purpose of this program is to create an instance of a Car object, accelarate it's speed attribute to 25,
and decelarate it's speed back to 0'''

import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 10")

# import the python program that has the Car class
import Car 

def main():
    # Create an instance of the Car object. A 1992 Ford.
    myCar = Car.Car(1992, "Ford")

    # Loop 5 times, calling the accelarate method and displaying the speed on each iteration
    print("Accelarating..")
    for i in range(1, 6):
        myCar.accelarate()
        print(myCar.get_speed(), "mph", sep=" ")

    print()

    # Loop 5 times, calling the brake method and displaying the speed on each iteration
    print("Braking..")
    for i in range(1, 6):
        myCar.brake()
        print(myCar.get_speed(), "mph", sep=" ")

main()

