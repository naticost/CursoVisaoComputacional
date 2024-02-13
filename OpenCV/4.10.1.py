import cv2 as cv
import numpy as np

webcam = cv.VideoCapture(0,cv.CAP_DSHOW)
qrDecoder = cv.QRCodeDetector()
img_final = cv.imread('Modulo 2 - Alunos\imagens/fit.jpg')

while True:
    img = webcam.read()[1]
    dados, pontos, imgReta = qrDecoder.detectAndDecode(img)

    if dados != "" :
        pts = np.int32(pontos)

        cv.polylines(img,pts,True,(0,255,0),3)

        imgReta = cv.resize(imgReta,None,fx=10,fy=10,interpolation=cv.INTER_NEAREST)

        x,y,w,h = 200,200,400,400

        ptsOrigem = [[0,0],[w,0],[w,h],[0,h]]

        matriz = cv.getPerspectiveTransform(np.float32(ptsOrigem),np.float32(pts))

        res = cv.warpPerspective(img_final,matriz,(640,480))

        if dados == "fit":
            img_cinza = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

            _, binarizado = cv.threshold(img_cinza, 1, 255, cv.THRESH_BINARY_INV)

            binarizado = cv.cvtColor(binarizado,cv.COLOR_GRAY2BGR)

            resultado_final = cv.bitwise_and(img,binarizado)

            resultado_final = cv.bitwise_or(resultado_final,res)

            cv.imshow('Resultado',resultado_final)

    cv.imshow('Original',img)
    
    tecla = cv.waitKey(1)

    if tecla == ord('q'):
            break