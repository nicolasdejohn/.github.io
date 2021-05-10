# Nicolas DeJohn | Chapter 13-7 Lab | April 22 2021

'''
The purpose of this program is to create a Calls class that will calculate the rate of long distance calls depending on the time
of day.  

'''
# Import tkinter and tkinter.messagebox
import tkinter
import tkinter.messagebox

#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 13")

class Calls:
    def __init__(self):

        # Create the window
        self.main_window = tkinter.Tk()

        # Title of program and window size
        self.main_window.title("Long Distance Calls")
        self.main_window.minsize(300,50)

        # Create the frame containers
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create the label and entry field
        self.minutesLabel = tkinter.Label(self.top_frame, text="Enter minutes: ")
        self.minutes = tkinter.Entry(self.top_frame, width = 6)

        # Pack the entry field
        self.minutesLabel.pack()
        self.minutes.pack()

        # Create an IntVar object to use with the Radiobuttons.
        self.radio_var = tkinter.IntVar()

        # Set the intVar object to 1.
        self.radio_var.set(1)

        # Create the set of radio buttons
        self.rb1 = tkinter.Radiobutton(self.mid_frame, text="Daytime", variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.mid_frame, text="Evening", variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.mid_frame, text="Off-Peak", variable=self.radio_var, value=3)

        # Pack the radio buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create a submit and quit button
        self.submitButton = tkinter.Button(self.bottom_frame, text="Submit Order", command=self.calculateRate)
        self.quitButton = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the buttons
        self.submitButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the main loop
        tkinter.mainloop()

    # Define calculateRate function
    def calculateRate(self):

        numMinutes = int(self.minutes.get())
        rate = 0

        if self.radio_var.get() == 1:
            rate = 0.07
        if self.radio_var.get() == 2:
            rate = 0.12
        if self.radio_var.get() == 3:
            rate = 0.05

        rateTotal = numMinutes * rate
        
        tkinter.messagebox.showinfo("Order Summary", "The cost of your call is $" + str(format(rateTotal, ".2f")))

            
