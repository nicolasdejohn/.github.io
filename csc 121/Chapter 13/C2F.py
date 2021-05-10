# Nicolas DeJohn | Chapter 13-4 Lab | April 22 2021

'''
The purpose of this program is to create a GUI Class that converts Celsius to Fahrenheit.  

'''
# Import tkinter assets
import tkinter
import tkinter.messagebox
#import collections
#import os 
#os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 13")

# Define the class
class C2F: 
    def __init__(self):

        # Create the window
        self.main_window = tkinter.Tk()

        # Title of program and window size
        self.main_window.title("Free C2F Converter")
        self.main_window.minsize(300,50)

        # Create the frame containers
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create the label and entry field
        self.celsiusLabel1 = tkinter.Label(self.top_frame, text="Enter Celsius: ")
        self.enterCelsius = tkinter.Entry(self.top_frame, width = 6)

        # Create the buttons
        self.convertButton = tkinter.Button(self.bottom_frame, text="Convert!", command=self.convert)
        self.quitButton = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the label and entry fields
        self.celsiusLabel1.pack(side='left')
        self.enterCelsius.pack(side='left')

        # Pack the buttons
        self.convertButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Initiate the main loop
        tkinter.mainloop()

    # Define the conversion formula
    def convert(self):
        celsius = float(self.enterCelsius.get())
        fahrenheit = (9/5*celsius) + 32
        
        # Display the results in a new window
        tkinter.messagebox.showinfo('Results', str(celsius) + " degrees celsius is " + str(fahrenheit) + " degrees fahrenheit.")