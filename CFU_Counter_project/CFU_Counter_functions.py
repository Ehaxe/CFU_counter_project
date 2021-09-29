# importing necessary libraries
import argparse
import cv2 as cv
import numpy as np
import imutils as im

# getting argument and parsing it
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="path to image")
parser.add_argument("-o", "--output", required=True, help="path to output")
args = parser.parse_args()

# loading of image in variable and printing of image size
image_orig = cv.imread(args["image"], cv.IMREAD_GRAYSCALE)
print ("size of image is: ", image_orig.shape)

# showing of image
cv.imshow("image", image_orig, image_gray)

cv.waitKey()

cv.imshow("Cropped image", image_crop)
# inputting of cropping of image for defining area to count, storing in image variable
def imageCrop (startX, endX, startY, endY):
    image_crop = image_orig[startX:endX, startY:endY]