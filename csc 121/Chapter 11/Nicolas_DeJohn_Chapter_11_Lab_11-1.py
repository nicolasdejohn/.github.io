# Nicolas DeJohn | Chapter 11-1 Lab | April 6 2021

'''The purpose of this program is to get information about an employee from the user and create a production worker object
from the data.'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 11")

# Import Employee.py
import Employee

# Initialize the variables that will be passed to the data attributes of the object
employeeName = input("Enter employee name: ")

# A few validation loops for the next set of data
while True:
    try:
        employeeNumber = int(input("Enter employee number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
while True:
    try:
        employeeShiftNumber = int(input("Enter employee shift (1 or 2): "))
        if employeeShiftNumber > 0 and employeeShiftNumber < 3:
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
            
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
while True:
    try:
        employeePayRate = float(input("Enter employee rate of pay: "))
        break
    except ValueError:
        print("Invalid input. Please enter re-enter rate of pay. ($0.00): ")

# Initialize an instance of the Production Worker object
employee1 = Employee.ProductionWorker(employeeName, employeeNumber, employeeShiftNumber, employeePayRate)

# Print the data
print()
print("Name: " + employee1.get_name())
print("Employee ID: ", employee1.get_number(), sep='')
print("Shift: ", employee1.get_shiftNumber(), sep='')
print("Pay Rate: $", format(employee1.get_payRate(), ',.2f'), sep='')