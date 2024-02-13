

import cv2 as cv
import numpy as np
from keras.models import load_model

modelo = load_model('FacesDetectadas.h5')
webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

emocao = ['neutro',
        'sorrindo',
        'surpreso']

detector = cv.CascadeClassifier('outros/haarcascade_frontalface_alt2.xml')
while True:
    img = webcam.read()[1]
    img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rostos = detector.detectMultiScale(img_cinza)
    for rosto in rostos:
        x,y,w,h = rosto
        face = img[y:y+h, x:x+w]

    cnnInput = cv.resize(face,(100,100))
    cv.imshow('mini imagem', cnnInput)
    cnnInput = cnnInput/255
    imgNumPy = np.array([cnnInput])
    inferencias = modelo.predict(imgNumPy, verbose=0)
    indice = np.argmax(inferencias[0])
    print(emocao[indice], inferencias[0][indice])

    texto = emocao[indice] + str(round(inferencias[0][indice],2))
    if inferencias[0][indice] > 0.5:
        cv.putText(img,texto,(10,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
    
    cv.imshow('Tela', img)
    tecla = cv.waitKey(1)
    if tecla == ord('q'):
        break