# Nicolas DeJohn | Chapter 13-6 Lab | April 22 2021

'''
The purpose of this program is to display a series of checkboxes for mechanical services and total up the cost for each service.  

'''
# Import tkinter and tkinter.messagebox
import tkinter
import tkinter.messagebox

import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 13")

# Define the class
class Order:
    def __init__(self):

        # Create the window
        self.main_window = tkinter.Tk()

        # Title of program and window size
        self.main_window.title("Order Processing")
        self.main_window.minsize(300,50)

        # Create the frame containers
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create seven IntVar objects
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Set each IntVar to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # Create seven check buttons
        self.cb1 = tkinter.Checkbutton(self.top_frame, text="Oil Change - $30", variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text="Lube Job - $20", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text="Radiator Flush - $40", variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text="Transmission Flush - $100", variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text="Inspection - $35", variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text="Muffler Replacement - $200", variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text="Tire Rotation - $20", variable=self.cb_var7)

        # Create a submit and quit button
        self.submitButton = tkinter.Button(self.bottom_frame, text="Submit Order", command=self.totalOrder)
        self.quitButton = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the checkboxes
        self.cb1.pack(side='top')
        self.cb2.pack(side='top')
        self.cb3.pack(side='top')
        self.cb4.pack(side='top')
        self.cb5.pack(side='top')
        self.cb6.pack(side='top')
        self.cb7.pack(side='top')

        # Pack the buttons
        self.submitButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Initialize the tkinter mainloop
        tkinter.mainloop()

    # Define the totalOrder function
    def totalOrder(self):
        subtotal = 0
        tax= 0.07

        # Get each checkbox and add the price to the total respectively
        if self.cb_var1.get() == 1:
            subtotal += 30
        if self.cb_var2.get() == 1:
            subtotal += 20
        if self.cb_var3.get() == 1:
            subtotal += 40
        if self.cb_var4.get() == 1:
            subtotal += 100
        if self.cb_var5.get() == 1:
            subtotal += 35
        if self.cb_var6.get() == 1:
            subtotal += 200
        if self.cb_var7.get() == 1:
            subtotal += 20

        # Calculate the total with tax
        totalTax = subtotal * tax
        total = subtotal + totalTax

        # Display the results
        tkinter.messagebox.showinfo("Order Summary", "Your order total is $" + str(format(total, '.2f')) + " with tax.")