#Treino Dados

import cv2 as cv
import os
import numpy as np
from keras.utils import to_categorical
from keras import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.callbacks import TensorBoard



webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

X = []
Y = []
diretorios = ['cap4/img/neutro/', 'cap4/img/sorrindo/', 'cap4/img/surpreso/']
for diretorio in diretorios:
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        img = cv.imread(diretorio+arquivo)
        detector = cv.CascadeClassifier('outros/haarcascade_frontalface_alt2.xml')
        imgCinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        rostos = detector.detectMultiScale(imgCinza)
        for x, y, w, h in rostos:
            face = img[y:y + h, x:x +w]

        if img is not None:
            img = cv.resize(face, (100,100))
            X.append(img)
            Y.append(diretorios.index(diretorio))

X = np.array(X)/255
Y = np.array(Y)

y_cat = to_categorical(Y)

modelo = Sequential()
modelo.add(Conv2D(50, (3, 3), activation='relu', input_shape=(100, 100, 3)))
modelo.add(MaxPooling2D((2, 2)))
modelo.add(Dropout(0.2))
modelo.add(Flatten())
modelo.add(Dense(200, activation='relu'))
modelo.add(Dropout(0.3))
modelo.add(Dense(3, activation='softmax'))
modelo.compile(optimizer='adam', 

              loss='categorical_crossentropy', 

              metrics=['accuracy'])

tbCallback = TensorBoard('logs')
modelo.fit(
    X, 
    y_cat, 
    batch_size=256, 
    epochs=30, 
    verbose=1, 
    validation_split=0.2,
    callbacks=[tbCallback]
)

modelo.save('FacesDetectadas.h5')