import tkinter as tk
import cv2
from tkinter import filedialog
from tkinter import *

HEIGHT = 800
WIDTH = 1200

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()
# #eeedef 
frame = tk.Frame(root, bg="black", width=400, height=HEIGHT) 
frame.place(relheight=1, relwidth=1) 

frame2 = tk.Frame(root, bg="blue") 
frame2.place(x=400, y=0, relwidth=1, relheight=1) 
 
 
 
# function defining the file selection process
def openFile():
    tk.filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) 
     
#def cfu_count():
    #define how to count spots with openCV

#root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print (root.filename)

# Label and Button for selecting and loading a file
labelButtonBrowse = tk.Label(root, text="Select file for CFU count:")
labelButtonBrowse.place(x=100, y=77)
buttonBrowse = tk.Button(root, text="Browse:", command=openFile)
buttonBrowse.place(x=100, y=100)
# entry box with selected file path shown
entryPath = tk.Entry(root, bg="white")
entryPath.place(x=165, y=104)

# Defining function for setting and calling slider
#def selSlide():
    #selectionSlide = "Value =" + str(slideVar.get())
    #label.config(text = selectionSlide)
# Label and Slider for sharpening the image
slideVar = tk.DoubleVar()
labelSharp = tk.Label(root, text="Change to adjust image sharpness:")
labelSharp.place(x=100, y=177)
slideSharp = tk.Scale(root, variable = slideVar, orient=HORIZONTAL, from_=0, to=100)
slideSharp.place(x=100, y=200)

#, sliderlength=200
# Label and Button for counting colonies from image selected
labelButtonColonies = tk.Label(root, text="Press to Count Colonies:")
labelButtonColonies.place(x=100, y=277)
buttonColonies = tk.Button(root, text="Count Colonies:")
buttonColonies.place(x=100, y=300)

# Label for entry of values to input into actual CFU calculation
labelEntryAmount = tk.Label(root, text="Input amount added in mL:")
labelEntryAmount.place(x=100, y=377)
entryAmount = tk.Entry(root, bg="white")
entryAmount.place(x=100, y=400)
# Label for entry of values to input into actual CFU calculation
labelEntryDilution = tk.Label(root, text="Input dilution used")
labelEntryDilution.place(x=100, y=377+50)
entryDilution = tk.Entry(root, bg="white")
entryDilution.place(x=100, y=400+50)


# Label and Button for calculating the actual CFU/mL
labelButtonCount = tk.Label(root, text="Press to Count CFU:")
labelButtonCount.place(x=100, y=527)
buttonCount = tk.Button(root, text="Count CFU:")
buttonCount.place(x=100, y=550)

#cv2.estimateChessboardSharpness()

root.mainloop()
