# importing critical libraries
import tkinter as tk
import webbrowser
import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
from tkinter import filedialog

# initializing main loop
root = tk.Tk()
root.title("CFU Counter")
root.geometry("1200x1200")
#root.resizable(width=False, height=False)



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

        # first drop-dwon menu
        firstMenu = tk.Menu(topBar, tearoff=0)
        firstMenu.add_command(label="Open image:", command=openCV.open_image)
        firstMenu.add_command(label="Exit", command=root.quit)
        topBar.add_cascade(label="File", menu=firstMenu)
        # second drop-dwon menu
        secondMenu = tk.Menu(topBar, tearoff=0)
        secondMenu.add_command(label="Set area (rectangle):", command=root.quit)
        secondMenu.add_command(label="Set area (polygon):", command=root.quit)
        secondMenu.add_command(label="Count Colonies:", command=root.quit)
        topBar.add_cascade(label="Processing", menu=secondMenu)
        # third drop-dwon menu
        thirdMenu = tk.Menu(topBar, tearoff=0)
        thirdMenu.add_command(label="ReadMe Online", command=self.openURL)
        topBar.add_cascade(label="Help", menu=thirdMenu)
        # forming menues
        root.config(menu=topBar)


# class for loading and managing images
class openCV():
    # importing important libraries
    


    def open_image():
        image_orig = cv2.imread(filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
        if len(image_orig) > 0:
            print ("yes")
        print ("image loaded")   
        image_gray = cv2.cvtColor(image_orig, cv2.COLOR_BGR2GRAY)
        
        #store image as variable and get dimensions
        height = image_gray.shape[0]
        width = image_gray.shape[1]
        print (height, width)
        
        image_canvas = tk.Canvas(root, width = width, height = height)
        image_canvas.grid()

        cv2.imshow("image_canvas", image_gray)

    def draw_polygon():
        pass

    def draw_rectangle():
        pass
    
    def count_CFU():
        pass

    
app = menuBar(root)
root.mainloop()
