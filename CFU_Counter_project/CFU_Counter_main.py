# importing critical libraries
import tkinter as tk
import webbrowser
import cv2
import numpy as np
#import Image, ImageTk
from tkinter import filedialog

# initializing main loop
root = tk.Tk()
root.title("CFU Counter")
root.geometry("1200x1200")
root.resizable(width=False, height=False)



# setting up class for defining a GUI frame
class menuBar(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.menu_widget()

    def openURL(self):
        url = "https://github.com/Ehaxe/CFU_counter_project/blob/main/README.md"
        new=1
        webbrowser.open(url,new=new)

        # creating the different menu widgets
    def menu_widget(self):

        topBar = tk.Menu(root)
        firstMenu = tk.Menu(topBar, tearoff=0)
        firstMenu.add_command(label="Open image:", command=openCV.open_image)
        firstMenu.add_command(label="Exit", command=root.quit)
        topBar.add_cascade(label="File", menu=firstMenu)

        secondMenu = tk.Menu(topBar, tearoff=0)
        secondMenu.add_command(label="Set area (rectangle):", command=root.quit)
        secondMenu.add_command(label="Set area (polygon):", command=root.quit)
        secondMenu.add_command(label="Count Colonies:", command=root.quit)
        topBar.add_cascade(label="Processing", menu=secondMenu)

        thirdMenu = tk.Menu(topBar, tearoff=0)
        thirdMenu.add_command(label="ReadMe Online", command=self.openURL)
        topBar.add_cascade(label="Help", menu=thirdMenu)
    
        root.config(menu=topBar)


# class for loading and manage images
class openCV():
    # importing important libraries
    


    def open_image():
        filedialog.askopenfile(initialdir = "/",title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))


    def draw_polygon():
        pass

    def draw_rectangle():
        pass
    
    def count_CFU():
        pass

    
app = menuBar(root)
root.mainloop()
