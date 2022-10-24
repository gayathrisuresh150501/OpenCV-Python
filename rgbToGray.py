import cv2 as cv


img =  cv.imread('Image/BirdCage.jpeg')
cv.imshow('Bird Cage', img)

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Bird Cage', gray_image)


cv.waitKey(0)