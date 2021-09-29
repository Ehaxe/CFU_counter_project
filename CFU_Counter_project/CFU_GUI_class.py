# importing of necessary libraries
from tkinter import *

# setting up class for defining a GUI frame
class CFU_GUI(Frame):
    # initializing class
    def __init__(self, master):
        # organizing gui
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets():
        # creating the actual widgets from tkinter
        menubar = Menu(root)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Select image", command=self.open_file)



