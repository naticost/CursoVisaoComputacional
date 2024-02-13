import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
detector = cv.QRCodeDetector()

while True:
    img = webcam.read()[-1]
    dados, pontos, imgReta = detector.detectAndDecode(img)

    if dados != "":
        pontos = np.int32(pontos)
        cv.polylines(img, pontos, True, (0, 0, 255), 3)
        imgReta = cv.resize(imgReta, None, fx=10, fy=10, interpolation=cv.INTER_NEAREST)
        cv.imshow("ImageReta", imgReta)

    print(dados)

    cv.imshow("Original", img)
    tecla = cv.waitKey(1)
    if tecla ==ord('q'):
        break