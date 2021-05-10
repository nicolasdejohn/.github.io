# Nicolas DeJohn | Chapter 11-3 Lab | April 6 2021

'''The purpose of this program is to create and display a customer object by passing basic info into it's data attributes'''

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 11")

# Import Person.py
import Person

# Initialize the variables that will be passed to the data attributes of the object
customerName = input("Enter customer name: ")
customerAddress = input("Enter customer's address: ")
customerPhoneNumber = input("Enter customer's phone number(XXX-XXX-XXXX): ")

# Validate that customerNumber is an integer
while True:
    try:
        customerNumber = int(input("Enter customer ID: "))
        break
    except ValueError:
        print("Invalid input. Enter only numbers.")

# Initialize onMailingList variable
onMailingList = True

# Ask the user if the customer is on the mailing list and validating only yes and no answers
while True:
    promptMailingList = input("Is this customer on mailing list?: ")
    if promptMailingList.lower() == "y":
        onMailingList = True
        break
    elif promptMailingList.lower() == "n":
        onMailingList = False
        break
    else:
        print("Invalid input. Please use 'Y', 'y', 'N', or 'n'.")

# Create an instance of the customer object
customer = Person.Customer(customerName, customerAddress, customerPhoneNumber, customerNumber, onMailingList)

# Display the customer object's attributes
print()
print("Name: ", customer.get_name(), sep="")
print("Address: ", customer.get_address(), sep="")
print("Phone: ", customer.get_phoneNumber(), sep="")
print("Customer ID: ", customer.get_customerNumber(), sep="")
print("Mailing List: ", customer.get_onMailingList(), sep="")


