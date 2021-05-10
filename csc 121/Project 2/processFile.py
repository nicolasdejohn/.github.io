# Nicolas DeJohn | Project 2 | May 5th 2021

''' 
   The purpose of this program is to process a text file with customer orders and display them in a GUI
    
''' 

import tkinter
import tkinter.messagebox
import calcOrder

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Project 2")

class processFile():
    def __init__(self, regular, grande, venti, plainCoffee, latte, macchiato, frappuccino, salesTax):

        self.regular = regular
        self.grande = grande
        self.venti = venti
        self.plainCoffee = plainCoffee
        self.latte = latte
        self. macchiato = macchiato
        self.frappuccino = frappuccino
        self.salesTax = salesTax

        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Order List")
        self.main_window.minsize(350,40)

        # Open the file for reading
        self.file = open("coffeeShopData.txt", "r")

        # Initialize an empty list to use for processing
        self.customerList = []

        # Initialize counters for the loop
        self.rowCounter = 0
        self.orderCounter = 1

        for i in self.file:
            if i != "\n":
                # Conditionals check what the string is and converts them to the appropriate value to the list
                if "8" in i:
                    self.customerList.append(self.regular)
                elif "16" in i:
                    self.customerList.append(self.grande)
                elif "24" in i:
                    self.customerList.append(self.venti)
                elif "plain coffee" in i.lower():
                    self.customerList.append(self.plainCoffee)
                elif "latte" in i.lower():
                    self.customerList.append(self.latte)
                elif "macchiato" in i.lower():
                    self.customerList.append(self.macchiato)
                elif "frappuccino" in i.lower():
                    self.customerList.append(self.frappuccino)
                else:
                    self.customerList.append(i.rstrip()) # This will append the customers name when no other condition is met
                    
            else:
                # Once the loop reaches a new line, it will process the data group for the current customer
                self.orderSubTotal = calcOrder.calculateSubtotal(self.customerList[2], self.customerList[1])
                self.orderTax = calcOrder.calculateTax(self.orderSubTotal, self.salesTax)
                self.orderTotal = calcOrder.calculateTotal(self.orderSubTotal, self.orderTax)
                
                # Render tkinter labels with appropriate data
                self.orderLB = tkinter.Label(self.main_window, text="Order " + str(self.orderCounter) + ":").grid(row=self.rowCounter, column=0, sticky='W', pady=0)
                self.customerLB = tkinter.Label(self.main_window, text=str(self.customerList[0])).grid(row=self.rowCounter + 1, column=1, sticky='W', pady=0)
                self.priceLB = tkinter.Label(self.main_window, text="Price of Coffee: $" + str(format(self.orderSubTotal, '0.2f'))).grid(row=self.rowCounter + 2, column=1, sticky='W', pady=0)
                self.taxLB = tkinter.Label(self.main_window, text="Sales Tax: $" + str(format(self.orderTax, '0.2f'))).grid(row=self.rowCounter + 3, column=1, sticky='W', pady=0)
                self.totalLB = tkinter.Label(self.main_window, text="Total Amount Owed: $" + str(format(self.orderTotal, '0.2f'))).grid(row=self.rowCounter + 4, column=1, sticky='W', pady=0)

                # Reset the list for the next loop
                self.customerList.clear()
                 
                self.orderCounter += 1

            self.rowCounter += 2

        # Close the file    
        self.file.close()

        # Exit the program
        self.okButton = tkinter.Button(self.main_window, text="OK", command=self.main_window.destroy).grid(row=self.rowCounter + 3, column=1, sticky='E', pady=2, ipadx=20)

        # Enter tkinter mainloop
        tkinter.mainloop()
