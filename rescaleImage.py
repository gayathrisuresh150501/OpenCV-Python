import cv2 as cv
import rescaleFunction as rf

img =  cv.imread('Image/BirdCage.jpeg')

rescaledImage = rf.rescaleFrame(img, 0.2)
cv.imshow('Bird Cage', rescaledImage)

cv.waitKey(0)