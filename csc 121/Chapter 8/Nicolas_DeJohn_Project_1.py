# Nicolas DeJohn | Project 1 | March 17th 2021

'''
The purpose of this program is to process customer coffee orders and convert data from the exisitng customer order text file.

'''
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 8")

# Initialize constants
plainCoffee = 0.23
latte = 0.33
macchiato = 0.35
frappuccino = 0.38
regular = 8
grande = 16
venti = 24
salesTax = 0.07

# Menu Option
def main():
    # Input validation loop
    while True: 
        print("Welcome to the World's Best Coffee Shop\n")
        print("1 - Process Order\n2 - Process a Data File\n3 - Quit\n")
        try:
            menuInput = int(input("Enter choice of action: "))
        except ValueError:
            print("Invalid response. Use only '1', '2', or '3'.")
            continue
        if menuInput == 1:
            orderInfo = processOrder(selectCoffee(), selectSize()) # Sets the value to the returned tuple
            customerName = input("Input customer name: ")
            print("\n" + customerName + "\nPrice of Coffee: $" + str(format(orderInfo[0], "0.2f")) + "\nSales Tax: $" + str(orderInfo[1]) + "\nTotal Amount Owed: $" + str(format(orderInfo[2], "0.2f")) + "\n")
        elif menuInput == 2:
            processData()
        elif menuInput == 3:
            print("The program has stopped.")
            break
        else:
            print("Invalid response. Use only '1', '2', or '3'.")

# Choose the coffee type
def selectCoffee():
    # Input validation loop
    while True:
        print("\n1 - Plain Coffee\n2 - Latte\n3 - Macchiato\n4 - Frappuccino\n")
        # Try statement ensures only numbers are used
        try:
            coffeeInput = int(input("Enter choice of coffee: "))
        except ValueError:
            print("Invalid response. Use only '1', '2', '3', or '4'.")
            continue
        # Conditional statement ensures only 1, 2, or 3 is used
        if coffeeInput == 1:
            costPerOunce = plainCoffee
            break
        elif coffeeInput == 2:
            costPerOunce = latte
            break
        elif coffeeInput == 3:
            costPerOunce = macchiato
            break
        elif coffeeInput == 4:
            costPerOunce = frappuccino
            break
        else:
            print("Invalid response. Use only '1', '2','3' or '4'.")
    return costPerOunce    

# Choose the size
def selectSize():
    # Input validation loop
    while True:
        print("\n1 - Regular\n2 - Grande\n3 - Venti\n")
        # Try statement ensures only numbers are used
        try:
            sizeInput = int(input("Enter choice of size: "))
        except ValueError:
            print("Invalid response. Use only '1', '2', '3'.")
            continue
        # Conditional statement ensures only 1, 2, or 3 is used and sets sizeInOz to the appropriate constant value
        if sizeInput == 1:
            sizeInOz = regular
            break
        elif sizeInput == 2:
            sizeInOz = grande
            break
        elif sizeInput == 3:
            sizeInOz = venti
            break
        else:
            print("Invalid response. Use only '1', '2', or '3'.")
    return sizeInOz

# Process the order
def processOrder(coffee, size):
    totalBeforeTax = coffee * size
    totalTax = round((totalBeforeTax * salesTax), 2)
    totalAfterTax = totalBeforeTax + totalTax
    return [totalBeforeTax, totalTax, totalAfterTax]
    

# Process the data from the text file
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