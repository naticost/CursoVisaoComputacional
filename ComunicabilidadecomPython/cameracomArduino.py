import cv2 as cv
import numpy as np
import serial
import time 

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

conexao = serial.Serial('COM5', baudrate= 9600)
time.sleep(2)

while True:
#Começo do tratamento
    img = webcam.read()[1]  #Necessário repetir o .read para mostra a foto mais atual
    img = webcam.read()[1]
    msg = conexao.read_all().decode('ascii')
    #print(msg)

    if 'foto' in msg :
        cv.imshow('img', img)
        cv.waitKey(1)
        mediaCores = cv.mean(img)
        print (mediaCores)

        if mediaCores[0] > mediaCores[1] and mediaCores[0] >  mediaCores[2] :
            cor = 'azul'
            conexao.write(cor.encode('ascii'))
            
        
        elif mediaCores[1] > mediaCores[0] and mediaCores[1] >  mediaCores[2] :
            cor = 'verde'
            conexao.write(cor.encode('ascii'))
            

        elif mediaCores[2] > mediaCores[1] and mediaCores[2] >  mediaCores[1] :
            cor = 'vermelho'
            conexao.write(cor.encode('ascii'))
        
        print(cor)
    
#Final do tratamento