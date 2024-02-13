import cv2 as cv
import numpy as np

def unsharp_mask(image,factor):
    blurred = cv.blur(image,(5,5))
    diff = cv.subtract(image, blurred)
    sharpened = cv.add(diff * factor, image)
    return sharpened

keys = {ord('q'):0, ord('w'):1, ord('e'):2, ord('r'):3, ord('s'):4 }

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
factor = 0

while True:
    img = webcam.read()[1]
    
    if factor < 0 :
        img = unsharp_mask(img, factor)
    cv.imshow('webcam', img)
    tecla = cv.waitKey(1)

    if tecla in keys:
        factor = keys[tecla]
        if factor == 4:
            break

webcam.release()
cv.destroyAllWindows()