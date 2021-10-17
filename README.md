# CFU_counter_project H1

## Table of contents H2
* [Introduction] (#introduction)
* [Necessary Packages] (#necessary-packages)
* [How to run the program] (#how-to-run-the-program)
* [Adjusting parameters for cell deterction] (#adjusting-parameters-for-cell-detection)

### Introduction H3
A graphical interface program for identifying and counting colonies on from a jpg file

#### Necessary packages H4
required packages are:
	numpy
	Pillow
	opencv-python
	tkinter
	webbrowser

##### How to run the program H5

Install necessary packages

Launch the CFU_Counter_main.py file
From the file menu select: open image to load an image
from Processing menu, select Count colonies, to count detected colonies

###### Adjusting parameters for cell detection H6

Open CFU_Counter_main.py file in IDE or selected word processor

Under open_CV class, count_CFU function, adjust parameters of: 
 
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
        