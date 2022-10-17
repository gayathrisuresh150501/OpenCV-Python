import cv2 as cv

img =  cv.imread('Image/BirdCage.jpeg')

cv.imshow('Bird Cage', img)

cv.waitKey(0)