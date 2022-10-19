import cv2 as cv
import numpy as np

blankImage = np.zeros((500, 500, 3), dtype = 'uint8')


cv.line(blankImage, (0, 0), (blankImage.shape[1]//2, blankImage.shape[0]//2), (0, 0, 255), thickness = 2)


cv.imshow('Drawing a line', blankImage)

cv.waitKey(0)