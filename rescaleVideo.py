import cv2 as cv
import rescaleFunction as rf

video = cv.VideoCapture('Video/cat.mp4')

while True:

    isTrue, frame = video.read()

    rescaledVideo = rf.rescaleFrame(frame, 0.2)
    cv.imshow('Video', rescaledVideo)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()