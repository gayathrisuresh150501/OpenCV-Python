import cv2 as cv
import numpy as np

blankImage = np.zeros((500, 500, 3), dtype = 'uint8')

# cv.imshow('Blank Window', blankImage) #to show blank window/blank screen

# blankImage[:] = 0, 0, 255  #to set the window color to red, here BGR format is followed
# cv.imshow('Red Window', blankImage)

# cv.rectangle(blankImage, (0,0), (blankImage.shape[1]//2, blankImage.shape[0]//2), (0, 0, 255), thickness = 2)  #to draw a hollow rectangle wrt coordinates

# cv.rectangle(blankImage, (0,0), (blankImage.shape[1]//2, blankImage.shape[0]//2), (0, 0, 255), thickness = -1) #to draw a solid rectangle wrt coordinates

# cv.rectangle(blankImage, (0,0), (250, 500), (0, 0, 255), thickness = 2) #to draw a hollow rectangle statically

# cv.rectangle(blankImage, (0,0), (250, 500), (0, 0, 255), thickness = -1)  #to draw a solid rectangle statically

cv.imshow('Drawing a rectangle', blankImage)

cv.waitKey(0)
