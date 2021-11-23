#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 12:52:21 2021

@author: bing
"""

from tkinter import *

class TempConverter:
    """
    A simple app for converting from Fahrenheit to Celsius
    """
    def __init__(self, parent):
        self.celsius_val = Label(parent, text="", width=20)
        self.celsius_val.grid(column=1, row=1)
        self.celsius_label = Label(parent, text="Celsius", width=20)
        self.celsius_label.grid(column=1, row=0)

        self.fahr_input = Entry(parent)
        self.fahr_input.grid(column=0, row=1)
        self.fahr_label = Label(parent, text="Fahrenheit")
        self.fahr_label.grid(column=0, row=0)

        self.convert_button = Button(parent, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, column=0)

        self.quit_button = Button(parent, text="Quit", comman=parent.destroy)
        self.quit_button.grid(row=2, column=1)
    
    def convert(self):
        # get the fahrenheit value from the widget and convert it from
        # a string to a float number
        dfahr = float(self.fahr_input.get())
        # calculate the celsius value as a float
        celsius = (dfahr-32)*5.0/9.0
        # update the celsius widget with the celsius value by
        # converting from a float to a string
        self.celsius_val.configure(text = str(celsius))

root = Tk()
app = TempConverter(root)
root.mainloop()