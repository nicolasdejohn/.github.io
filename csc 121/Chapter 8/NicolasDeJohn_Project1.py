# Nicolas DeJohn | Project 1 | March 17th 2021

'''
The purpose of this program is to process customer coffee orders.

'''

import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")


# Global constants
salesTax = 0.07
pricePerOz = 0
sizeInOz = 0

# Main function
def main():
    mainMenu()

# Menu option
def mainMenu():
    while True:
        print("Welcome to the World's Best Coffee Shop\n")
        print("1 - Process Order\n2 - Process a Data File\n3 - Quit\n")
        try:
            menuInput = int(input("Enter choice of action: "))
        except ValueError:
            print("Invalid response. Use only '1', '2', or '3'.")
            continue
        if menuInput == 1:
            cost = determinePricePerOunce(pricePerOz)
            size = determineSizeOunces(sizeInOz)
            #customerName = input("\nEnter the name of the customer: ")
            total = calculateTotal(calculateSubTotal(cost, size), calculateTax(calculateSubTotal(cost,size), salesTax))
            print(total)
        elif menuInput == 2:
            processOrder()
        elif menuInput == 3:
            print("exiting..")
            break
        else:
            print("Invalid response. Use only '1', '2', or '3'.")

# Choose a coffee type
def determinePricePerOunce(ounce):
    while True:
        print("\n1 - Plain Coffee\n2 - Latte\n3 - Macchiato\n4 - Frappuccino\n")
        try:
            menuInput = int(input("Enter choice of coffee: "))
        except ValueError:
            print("Invalid response. Use only '1', '2', '3', or '4'.")
            continue
        if menuInput == 1:
            ounce = 0.23
            break
        elif menuInput == 2:
            ounce = 0.33
            break
        elif menuInput == 3:
            ounce = 0.35
            break
        elif menuInput == 4:
            ounce = 0.38
            break
        else:
            print("Invalid response. Use only '1', '2','3' or '4'.")
    return ounce

# Choose a size      
def determineSizeOunces(size):
    while True:
        print("\n1 - Regular\n2 - Grande\n3 - Venti\n")
        try:
            menuInput = int(input("Enter choice of size: "))
        except ValueError:
            print("Invalid response. Use only '1', '2', '3'.")
            continue
        if menuInput == 1:
            size = 8
            break
        elif menuInput == 2:
            size = 16
            break
        elif menuInput == 3:
            size = 24
            break
        else:
            print("Invalid response. Use only '1', '2', or '3'.")
    return size

# Calculate Sub Total        
def calculateSubTotal(price, size):
    total = price * size
    return total

# Calculate Tax
def calculateTax(total, tax):
    totalTax = total * tax
    return totalTax

# Calculate total after tax
def calculateTotal(total, tax):
    totalOrder = total + tax
    return totalOrder

# Reads from file
def processData():

    # opens the file for reading
    file = open("coffeeShopData.txt", "r") 

    # I use this because it's easy to pull data from and to store converted strings
    customerList = [] 

    # Loops through the file and converts the strings in the file to the constant floats
    for i in file:    
        if i != "\n":
            # Conditionals check what the string is and converts them to the appropriate value to the list
            if "8" in i:
                customerList.append(regular)
            elif "16" in i:
                customerList.append(grande)
            elif "24" in i:
                customerList.append(venti)
            elif "plain coffee" in i.lower():
                customerList.append(plainCoffee)
            elif "latte" in i.lower():
                customerList.append(latte)
            elif "macchiato" in i.lower():
                customerList.append(macchiato)
            elif "frappuccino" in i.lower():
                customerList.append(frappuccino)
            else:
                customerList.append(i.rstrip()) # This will append the customers name when no other condition is met
        else:
            # Once the loop reaches a new line, it will process and print the grouping for that customer
            orderInfo = processOrder(customerList[1], customerList[2])
            print("\n" + customerList[0] + "\nPrice of Coffee: $" + str(format(orderInfo[0], "0.2f")) + "\nSales Tax: $" + str(orderInfo[1]) + "\nTotal Amount Owed: $" + str(format(orderInfo[2], "0.2f")) + "\n")
            customerList.clear() # Resets the list for the next loop
    file.close()


main()