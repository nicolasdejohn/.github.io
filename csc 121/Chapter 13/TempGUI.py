# Nicolas DeJohn | Chapter 13-4 Lab | April 22 2021

'''
The purpose of this program is  

'''
import tkinter
import tkinter.messagebox
import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 13")


class TempGUI: 
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.title("Free C2F Converter")
        self.main_window.minsize(300,50)

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.celsiusLabel1 = tkinter.Label(self.top_frame, text="Enter Celsius: ")
        self.enterCelsius = tkinter.Entry(self.top_frame, width = 12)

        self.convertButton = tkinter.Button(self.bottom_frame, text="Convert!", command=self.convert)
        self.quitButton = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.celsiusLabel1.pack(side='left')
        self.enterCelsius.pack(side='left')
        self.convertButton.pack(side='left')
        self.quitButton.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):

        celsius = float(self.enterCelsius.get())
        fahrenheit = (9/5*celsius) + 32

        tkinter.messagebox.showinfo('Results', str(celsius) + " degrees celsius is " + str(fahrenheit) + " degrees fahrenheit.")