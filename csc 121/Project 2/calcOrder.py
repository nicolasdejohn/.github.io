# Nicolas DeJohn | Project 2 | May 5th 2021

''' 
   The purpose of this program is to create some general functions that will process the price and tax of orders
    
''' 

#import collections
#import os
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Project 2")

# Function that calculates the subtotal
def calculateSubtotal(price, size):
    subtotal = price * size
    return subtotal

# Function that calculates the total tax
def calculateTax(total, tax):
    totalTax = total * tax
    return totalTax
    
    # Function that calculates the subtotal plus tax
def calculateTotal(total, tax):
    totalOrder = total + tax
    return totalOrder

