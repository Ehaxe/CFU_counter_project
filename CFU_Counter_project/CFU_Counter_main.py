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
root.geometry("250x0")
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
        #secondMenu.add_command(label="Set area (rectangle):", command=openCV.draw_rectangle)
        #secondMenu.add_command(label="Set area (polygon):", command=root.quit)
        secondMenu.add_command(label="Count Colonies:", command=openCV.count_CFU)
        topBar.add_cascade(label="Processing", menu=secondMenu)
        # third drop-dwon menu
        thirdMenu = tk.Menu(topBar, tearoff=0)
        thirdMenu.add_command(label="ReadMe Online", command=self.openURL)
        topBar.add_cascade(label="Help", menu=thirdMenu)
        # forming menues
        root.config(menu=topBar)


# class for loading and managing images
class openCV():
    
    def open_image():
        #using filedialog to open path dialog and passing it to c2.imread function
        img_orig = cv2.imread(filedialog.askopenfilename(initialdir = "/",title = "Select image",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
        if len(img_orig) > 0:
            print ("yes")
            print ("image loaded")
        #convert and store loaded image as grayscale image and make it global
        global img_gray
        img_gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        
        

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
        global img_canvas
        # convert to Pillow      
        Pil_img = PIL.Image.fromarray(img_gray)        
        TK_img = PIL.ImageTk.PhotoImage(image=Pil_img)        
        # create canvas to frame image and place image within canvas
        img_canvas = tk.Canvas(root, width = width, height = height)              
        img_canvas.create_image(0,0, image=TK_img, anchor=tk.NW)        
        img_canvas.grid()
        
     
    def count_CFU():

        # setting of parameters for blob detection
        params = cv2.SimpleBlobDetector_Params()
        # set threshold or intensity values for blob detection
        params.minThreshold = 100;
        params.maxThreshold = 20000;
        # set parameter for area size of blob detection
        params.filterByArea = True
        params.minArea = 20
        # set parameter for circularity or roundness of blobs
        params.filterByCircularity = True
        params.minCircularity = 0.2
        # set parameter for convexity (if circle is whole circle or parts of circle)
        params.filterByConvexity = True
        params.minConvexity = 0.85
        # set parameter for inertia or how elipsoid the shape is
        params.filterByInertia = True
        params.minInertiaRatio = 0.01
        # set up actual blob detector and draw them on image
        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(img_gray)
        img_with_keypoints = cv2.drawKeypoints(img_gray, keypoints, np.array([]), (0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        # opencv image show to compare to pillow
        cv2.imshow("image_canvas", img_with_keypoints)
        print (len(keypoints))        
        Pil_circle_img = PIL.Image.fromarray(img_with_keypoints)        
        TK_circle_img = PIL.ImageTk.PhotoImage(image=Pil_circle_img)
        #img_canvas.itemconfigure(img_canvas,image=TK_circle_img)

        # create and display CFU count values
        colony_count = "Number of colonies: "+str(len(keypoints))
        print (colony_count)
        tk.messagebox.showinfo(title="Colony count", message=colony_count)
        
    
app = menuBar(root)
root.mainloop()
