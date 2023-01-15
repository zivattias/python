from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

stimulator_window = Tk()
stimulator_window.geometry('600x600')
stimulator_window.title('PyCode')

heading = Label(stimulator_window,text='Welcome to the Text Editor',font=('bold',20),bg='light grey') # This will create a label for the heading.
heading.pack() # You have to pack this label so that it can be seen in the window

stimulator_window.mainloop()