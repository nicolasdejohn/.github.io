# Nicolas DeJohn | Project 2 | May 5th 2021

''' 
   The purpose of this program is to display the menu screen of the coffee shop app in a GUI
    
''' 

import tkinter
import tkinter.messagebox
import processOrder
import processFile

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Project 2")

# Global constants
salesTax = 0.07
plainCoffee = 0.23
latte = 0.33
macchiato = 0.35
frappuccino = 0.38
regular = 8
grande = 16
venti = 24

class App():
    def __init__(self):

        # Create the main window
        self.window = tkinter.Tk()
        self.window.title("World's Best Coffee Shop")
        self.window.minsize(350,50)
        self.titlePrompt = tkinter.Label(self.window, text="What would you like to do?" ).grid(row=0, column=0, sticky="W", pady=2, padx=10)

        # Create radio button variables and set it to 1
        self.radioVar = tkinter.IntVar()
        self.radioVar.set(1)

        # Create the radio buttons
        self.r1 = tkinter.Radiobutton(self.window, text="Process Order ", variable=self.radioVar, value=1).grid(row=1, column=0, sticky='W', pady=2, padx=10)
        self.r2 = tkinter.Radiobutton(self.window, text="Process File ", variable=self.radioVar, value=2).grid(row=2, column=0, sticky='W', pady=2, padx=10)

        # Create the submit and quit buttons
        self.submitButton = tkinter.Button(self.window, text="Submit", command=self.processChoice, width=15).grid(row=3, column=1, sticky="W", pady=2, padx=10)
        self.quitButton = tkinter.Button(self.window, text="Quit Program", command=self.window.destroy, width=15).grid(row=3, column=2, sticky="W", pady=2, padx=10)

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Function that processes the users choice
    def processChoice(self):
        choice = self.radioVar.get()
        if choice == 1:
            processOrder.Order(regular, grande, venti, plainCoffee, latte, macchiato, frappuccino, salesTax)
        else:
            order = processFile.processFile(regular, grande, venti, plainCoffee, latte, macchiato, frappuccino, salesTax)





