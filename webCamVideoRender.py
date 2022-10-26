# from pyflycap2.interface import Camera
import cv2 as cv

cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame =  cap.read()

    cv.imshow('Webcam', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv.destroyAllWindows()