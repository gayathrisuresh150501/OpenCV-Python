# from pyflycap2.interface import Camera
import cv2 as cv

def take_photo():
    cap = cv.VideoCapture(0)

    ret, frame = cap.read()
    cv.imwrite('webcampic.jpg', frame)
    cap.release()

take_photo()


