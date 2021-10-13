# importing critical libraries
import tkinter as tk
import webbrowser
import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
from tkinter import filedialog
import time

# initializing main loop
root = tk.Tk()
root.title("CFU Counter")
root.geometry("200x100")
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

        # first drop-dwon menu
        firstMenu = tk.Menu(topBar, tearoff=0)
        firstMenu.add_command(label="Open image:", command=openCV.open_image)
        firstMenu.add_command(label="Exit", command=root.quit)
        topBar.add_cascade(label="File", menu=firstMenu)
        # second drop-dwon menu
        secondMenu = tk.Menu(topBar, tearoff=0)
        secondMenu.add_command(label="Set area (rectangle):", command=openCV.draw_rectangle)
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
        img_orig = cv2.imread(filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
        if len(img_orig) > 0:
            print ("yes")
            print ("image loaded")   
            img_gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        
            detector = cv2.SimpleBlobDetector_create()
            keypoints = detector.detect(img_gray)
            img_with_keypoints = cv2.drawKeypoints(img_gray, keypoints, np.array([]), (0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

            # store image as variable and get dimensions
            height = img_gray.shape[0]
            width = img_gray.shape[1]
            print (height, width)
            # add extra spacing around edge
            gheight = height+2
            gwidth = width+2
            # dynamically set root window dimensions
            geometry = str(gwidth)+"x"+str(gheight)
            root.geometry(geometry)

            # define TK_img as global variable to prevent garbage collection
            global TK_img
            # convert to Pillow      
            Pil_img = PIL.Image.fromarray(img_gray)        
            TK_img = PIL.ImageTk.PhotoImage(image=Pil_img)        
            # create canvas to frame image and place image within canvas
            img_canvas = tk.Canvas(root, width = width, height = height, bg="black")              
            img_canvas.create_image(0,0, image=TK_img, anchor=tk.NW)
            img_canvas.grid(row=1)
        
        
            # opencv image show to compare to pillow
            cv2.imshow("image_canvas", img_with_keypoints)
        else:
            return

    def draw_polygon():
        pass

    top_left_corner=[]
    bottom_right_corner=[]

    def draw_rectangle(action, x, y, flags, *userdata):
        
        global top_left_corner, bottom_right_corner
        if action == cv2.EVENT_LBUTTONDOWN:
            top_left_corner = [(x,y)]
        elif action == cv2.EVENT_LBUTTONUP:
            bottom_right_corner = [(x,y)]
            cv2.rectangle(image_gray, top_left_corner[0], bottom_right_corner[0], (255,255,255), 2, 5)
    
    def count_CFU():
        pass

    
app = menuBar(root)
root.mainloop()
