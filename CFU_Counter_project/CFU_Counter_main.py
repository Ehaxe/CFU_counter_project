# importing critical libraries
import CFU_GUI_class
from tkinter import *

object = CFU_GUI_class.CFU_GUI

# initializing main loop
root = Tk()
root.title("CFU Counter")
root.geometry("800x1200")
root.resizable(width=False, height=False)
app = object(root)
root.mainloop()
