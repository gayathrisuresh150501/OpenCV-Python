import cv2 as cv
import numpy as np

blankImage = np.zeros((500, 500, 3), dtype = 'uint8')

# cv.circle(blankImage, (blankImage.shape[1]//2, blankImage.shape[0]//2), 50, (0, 0, 255), thickness = 2)

cv.circle(blankImage, (blankImage.shape[1]//2, blankImage.shape[0]//2), 50, (0, 0, 255), thickness = -1)


cv.imshow('Drawing a circle', blankImage)

cv.waitKey(0)
