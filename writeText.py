import cv2 as cv
import numpy as np

blankImage = np.zeros((500, 500, 3), dtype = 'uint8')


cv.putText(blankImage, "Hello World!", (blankImage.shape[1]//3, blankImage.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255), 2)


cv.imshow('Writing a text', blankImage)

cv.waitKey(0)