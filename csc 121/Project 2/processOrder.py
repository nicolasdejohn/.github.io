# Nicolas DeJohn | Project 2 | May 5th 2021

''' 
   The purpose of this program is to take an order and display the total in a GUI
    
''' 

import tkinter
import tkinter.messagebox
import calcOrder

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Project 2")

class Order():
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
        self.main_window.title("Process Order")
        self.main_window.minsize(350,100)

        # Create an IntVar object to use with the Radiobuttons.
        self.radio_var = tkinter.IntVar(self.main_window)
        self.radio_var2 = tkinter.IntVar(self.main_window)

        # Set the intVar objects to 1.
        self.radio_var.set(1)
        self.radio_var2.set(1)

        self.nameVar = tkinter.StringVar(self.main_window)
        self.nameVar.set("None")
        self.calcSubTotal = tkinter.StringVar(self.main_window)
        self.calcSubTotal.set("$0.00")
        self.calcTax = tkinter.StringVar(self.main_window)
        self.calcTax.set("$0.00")
        self.calcTotal = tkinter.StringVar(self.main_window)
        self.calcTotal.set("$0.00")

        

        # Create the set of radio buttons for coffee and pack them with .grid()
        self.coffee_label = tkinter.Label(self.main_window, text="Coffee Type:", font='Helvetica 10 bold').grid(row=0, column=0, sticky='W', pady=2)
        self.rb1 = tkinter.Radiobutton(self.main_window, text="Plain Coffee ", variable=self.radio_var, value=1, tristatevalue=1).grid(row=1, column=0, sticky='W', pady=2, padx=10)
        self.rb2 = tkinter.Radiobutton(self.main_window, text="Latte", variable=self.radio_var, value=2, tristatevalue=2).grid(row=2, column=0, sticky='W', pady=2, padx=10)
        self.rb3 = tkinter.Radiobutton(self.main_window, text="Macchiato", variable=self.radio_var, value=3, tristatevalue=3).grid(row=3, column=0, sticky='W', pady=2, padx=10)
        self.rb4 = tkinter.Radiobutton(self.main_window, text="Frappuccino", variable=self.radio_var, value=4, tristatevalue=4).grid(row=4, column=0, sticky='W', pady=2, padx=10)

        # Create labels that tell the user the price for each coffee type and pack them with .grid()
        self.lb1 = tkinter.Label(self.main_window, text="$0.23/oz").grid(row=1, column=1, sticky="W", pady=2)
        self.lb1 = tkinter.Label(self.main_window, text="$0.33/oz").grid(row=2, column=1, sticky="W", pady=2)
        self.lb1 = tkinter.Label(self.main_window, text="$0.35/oz").grid(row=3, column=1, sticky="W", pady=2)
        self.lb1 = tkinter.Label(self.main_window, text="$0.38/oz").grid(row=4, column=1, sticky="W", pady=2)

        # Create radio buttons for the size and pack them with .grid()
        self.size_label = tkinter.Label(self.main_window, text="Size:", font='Helvetica 10 bold').grid(row=0, column=2, sticky='W', pady=2)
        self.rb1 = tkinter.Radiobutton(self.main_window, text="Regular", variable=self.radio_var2, value=1, tristatevalue=1).grid(row=1, column=2, sticky='W', pady=2, padx=10)
        self.rb2 = tkinter.Radiobutton(self.main_window, text="Grande", variable=self.radio_var2, value=2, tristatevalue=2).grid(row=2, column=2, sticky='W', pady=2, padx=10)
        self.rb3 = tkinter.Radiobutton(self.main_window, text="Venti", variable=self.radio_var2, value=3, tristatevalue=3).grid(row=3, column=2, sticky='W', pady=2, padx=10)

        # Create labels that tell the user how many ounces in each size and pack them with .grid()
        self.lb1 = tkinter.Label(self.main_window, text="8 oz").grid(row=1, column=3, sticky="W", pady=2)
        self.lb1 = tkinter.Label(self.main_window, text="16 oz").grid(row=2, column=3, sticky="W", pady=2)
        self.lb1 = tkinter.Label(self.main_window, text="24 oz").grid(row=3, column=3, sticky="W", pady=2)

        # Create a prompt for customer name
        self.namePrompt = tkinter.Label(self.main_window, text="Enter name:", font='Helvetica 10 bold').grid(row=5, column=0, sticky="W", pady=2)
        self.name = tkinter.Entry(self.main_window, width=20)
        self.name.grid(row=6, column=0, sticky="W", pady=2, padx=10)

        # Create labels and an output field based on user input
        self.nameLB = tkinter.Label(self.main_window, text="Name:").grid(row=7, column=2, sticky="W", pady=2, padx=10)
        self.getNameLB = tkinter.Label(self.main_window, textvariable=self.nameVar).grid(row=7, column=3, sticky="W", pady=2)
        self.subTotalLB1 = tkinter.Label(self.main_window, text="Price of Coffee:").grid(row=8, column=2, sticky="W", pady=2, padx=10)
        self.subTotalLB2 = tkinter.Label(self.main_window, textvariable=self.calcSubTotal).grid(row=8, column=3, sticky="W", pady=2)
        self.taxLB1 = tkinter.Label(self.main_window, text="Sales Tax:").grid(row=9, column=2, sticky="W", pady=2, padx=10)
        self.taxLB1 = tkinter.Label(self.main_window, textvariable=self.calcTax).grid(row=9, column=3, sticky="W", pady=2)
        self.totalLB1 = tkinter.Label(self.main_window, text="Total Amount Owed:").grid(row=10, column=2, sticky="W", pady=2, padx=10)
        self.totalLB2 = tkinter.Label(self.main_window, textvariable=self.calcTotal).grid(row=10, column=3, sticky="W", pady=2)

        # Create the buttons and pack them with .grid()
        self.submitButton = tkinter.Button(self.main_window, text="Process Order", command=self.processData).grid(row=6, column=2, sticky='E', pady=2)
        self.quitButton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy).grid(row=6, column=3, sticky='E', pady=2, ipadx=20)

        # Enter the main loop
        tkinter.mainloop()

    # Function that outputs the users total
    def processData(self):
        cost = self.determinePrice()
        size = self.determineSize()
        total = calcOrder.calculateTotal(calcOrder.calculateSubtotal(cost, size), calcOrder.calculateTax(calcOrder.calculateSubtotal(cost, size), self.salesTax))

        self.nameVar.set(self.name.get())
        self.calcSubTotal.set("$" + format(calcOrder.calculateSubtotal(cost, size), '.2f'))
        self.calcTax.set("$" + format(calcOrder.calculateTax(calcOrder.calculateSubtotal(cost, size), self.salesTax), '.2f'))
        self.calcTotal.set("$" + format(total, '.2f'))
        

    # Function that sets the price based on coffee choice
    def determinePrice(self):
        userChoice = self.radio_var.get()
        if userChoice == 1:
            price = self.plainCoffee
        elif userChoice == 2:
            price = self.latte
        elif userChoice == 3:
            price = self.macchiato
        else:
            price = self.frappuccino
        return price
    
    # Function that sets the size in ounces based on size choice
    def determineSize(self):
        userChoice = self.radio_var2.get()
        if userChoice == 1:
            size = self.regular
        elif userChoice == 2:
            size = self.grande
        else:
            size = self.venti
        return size

        