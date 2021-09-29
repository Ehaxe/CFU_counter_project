# importing necessary libraries
import argparse
import cv2 as cv
import numpy as np
import imutils as im

# getting arguement and parsing it
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="path to image")
parser.add_argument("-o", "--output", required=True, help="path to output")
args = vars(parser.parse_args())

# loading of image
image_orig =cv.imread(args["image"])
height_orig, width.orig = image_orig.shape[:2]