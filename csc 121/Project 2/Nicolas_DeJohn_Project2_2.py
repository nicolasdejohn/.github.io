# Nicolas DeJohn | Project 2 | March 5th 2021

''' 
    The purpose of this program is to either process a customer order or read orders from a file and display them in a GUI

'''
import tkinter
import tkinter.messagebox



import collections
import os
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Project 2")

salesTax = 0.07
plainCoffee = 0.23
latte = 0.33
macchiato = 0.35
frappuccino = 0.38
regular = 8
grande = 16
venti = 24
  
master = tkinter.Tk()
master.title("World's Best Coffee Shop")
master.minsize(350,50)

# Function that processes the customer order
def processOrder():
    # Create new window  
    orderWindow= tkinter.Toplevel(master)
    orderWindow.title("Process Order")
    orderWindow.minsize(350,50)

    # Create an IntVar object to use with the Radiobuttons.
    coffee_var = tkinter.IntVar()
    size_var = tkinter.IntVar()

    # Set the intVar objects to 1.
    coffee_var.set(1)
    size_var.set(1)

    # Create the set of radio buttons for coffee and pack them with .grid()
    coffee_label = tkinter.Label(orderWindow, text="Coffee Type:").grid(row=0, column=0, sticky='W', pady=2)
    rb1 = tkinter.Radiobutton(orderWindow, text="Plain Coffee ", variable=coffee_var, value=1, tristatevalue=1).grid(row=1, column=0, sticky='W', pady=2, padx=10)
    rb2 = tkinter.Radiobutton(orderWindow, text="Latte", variable=coffee_var, value=2, tristatevalue=2).grid(row=2, column=0, sticky='W', pady=2, padx=10)
    rb3 = tkinter.Radiobutton(orderWindow, text="Macchiato", variable=coffee_var, value=3, tristatevalue=3).grid(row=3, column=0, sticky='W', pady=2, padx=10)
    rb4 = tkinter.Radiobutton(orderWindow, text="Frappuccino", variable=coffee_var, value=4, tristatevalue=4).grid(row=4, column=0, sticky='W', pady=2, padx=10)

    # Create labels that tell the user the price for each coffee type and pack them with .grid()
    priceLB1 = tkinter.Label(orderWindow, text="$0.23/oz").grid(row=1, column=1, sticky="W", pady=2)
    priceLB2 = tkinter.Label(orderWindow, text="$0.33/oz").grid(row=2, column=1, sticky="W", pady=2)
    priceLB3 = tkinter.Label(orderWindow, text="$0.35/oz").grid(row=3, column=1, sticky="W", pady=2)
    priceLB4 = tkinter.Label(orderWindow, text="$0.38/oz").grid(row=4, column=1, sticky="W", pady=2)

    # Create radio buttons for the size and pack them with .grid()
    size_label = tkinter.Label(orderWindow, text="Size:").grid(row=0, column=2, sticky='W', pady=2)
    rb5 = tkinter.Radiobutton(orderWindow, text="Regular", variable=size_var, value=1, tristatevalue=1).grid(row=1, column=2, sticky='W', pady=2, padx=10)
    rb6 = tkinter.Radiobutton(orderWindow, text="Grande", variable=size_var, value=2, tristatevalue=2).grid(row=2, column=2, sticky='W', pady=2, padx=10)
    rb7 = tkinter.Radiobutton(orderWindow, text="Venti", variable=size_var, value=3, tristatevalue=3).grid(row=3, column=2, sticky='W', pady=2, padx=10)

    # Create labels that tell the user how many ounces in each size and pack them with .grid()
    sizeLB1 = tkinter.Label(orderWindow, text="8 oz").grid(row=1, column=3, sticky="W", pady=2)
    sizeLB2 = tkinter.Label(orderWindow, text="16 oz").grid(row=2, column=3, sticky="W", pady=2)
    sizeLB3 = tkinter.Label(orderWindow, text="24 oz").grid(row=3, column=3, sticky="W", pady=2)

    # Function that will process the order
    def processData():
        cost = determinePrice()
        size = determineSize()
        total = calculateTotal(calculateSubtotal(cost, size), calculateTax(calculateSubtotal(cost, size), salesTax))
        tkinter.messagebox.showinfo("Order total", "Your total is $" + str(format(total, ".2f")))
        #tkinter.messagebox.showinfo("message", coffee_var.get())

    # Function that determines the price per oz
    def determinePrice():
        userChoice = coffee_var.get()
        if userChoice == 1:
            price = plainCoffee
        elif userChoice == 2:
            price = latte
        elif userChoice == 3:
            price = macchiato
        else:
            price = frappuccino
        return price

    # Function that determines the size in oz
    def determineSize():
        userChoice = size_var.get()
        if userChoice == 1:
            size = regular
        elif userChoice == 2:
            size = grande
        else:
            size = venti
        return size

    # Create buttons to process the order or quit this program
    orderButton = tkinter.Button(orderWindow, text="Process Order", command=processData).grid(row=5, column=2, sticky='E', pady=2, padx=10)
    quitButton = tkinter.Button(orderWindow, text="Quit", command=orderWindow.destroy).grid(row=5, column=3, sticky='E', pady=2, ipadx=20)

# Function that processes the file
def processFile():
    # Create new window
    fileWindow= tkinter.Toplevel(master)
    fileWindow.title("Process Order")
    fileWindow.minsize(350,50)

    # Opens the file for reading
    file = open("coffeeShopData.txt", "r") 

    # I use this because it's easy to pull data from and to store converted strings
    customerList = [] 

    # Loops through the file and converts the strings in the file to the constant floats
    rowCounter = 0 # Initialize some counters to use for tkinter rendering
    orderCounter = 1 # Same as above
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
            orderSubTotal = calculateSubtotal(customerList[2], customerList[1])
            orderTax = calculateTax(orderSubTotal, salesTax)
            orderTotal = calculateTotal(orderSubTotal, orderTax)
            
            # Render tkinter labels with appropriate data
            orderLB = tkinter.Label(fileWindow, text="Order " + str(orderCounter) + ":").grid(row=rowCounter, column=0, sticky='W', pady=0)
            customerLB = tkinter.Label(fileWindow, text=str(customerList[0])).grid(row=rowCounter + 1, column=1, sticky='W', pady=0)
            priceLB = tkinter.Label(fileWindow, text="Price of Coffee: $" + str(format(orderSubTotal, '0.2f'))).grid(row=rowCounter + 2, column=1, sticky='W', pady=0)
            taxLB = tkinter.Label(fileWindow, text="Sales Tax: $" + str(format(orderTax, '0.2f'))).grid(row=rowCounter + 3, column=1, sticky='W', pady=0)
            totalLB = tkinter.Label(fileWindow, text="Total Amount Owed: $" + str(format(orderTotal, '0.2f'))).grid(row=rowCounter + 4, column=1, sticky='W', pady=0)

            # Reset the list for the next loop
            customerList.clear() 
            orderCounter += 1

        rowCounter += 2
        
    file.close()
    # Exit the program
    okButton = tkinter.Button(fileWindow, text="Ok", command=fileWindow.destroy).grid(row=rowCounter + 3, column=1, sticky='E', pady=2, ipadx=20)

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

# Main menu buttons  
processOrderButton = tkinter.Button(master, text="Process Order", command=processOrder, width=15).grid(row=1, column=1, sticky="W", pady=2, padx=10)
processFileButton = tkinter.Button(master, text="Process File", command=processFile, width=15).grid(row=1, column=2, sticky="W", pady=2, padx=10)
quitButton = tkinter.Button(master, text="Quit", command=master.destroy, width=15).grid(row=1, column=3, sticky="W", pady=2, padx=10)

# Enter tkinter mainloop        
tkinter.mainloop()
