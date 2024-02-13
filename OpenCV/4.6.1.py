import cv2 as cv
import numpy as np

img = cv.imread('imagens/formatos.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
contours, hierarquia = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.02 * cv.arcLength(contour, True)
    aproximacao = cv.approxPolyDP(contour, epsilon, True)

    if cv.isContourConvex(aproximacao):
        cv.drawContours(img, [aproximacao], 0, (0,255,0), 2)
    else: cv.drawContours(img, [aproximacao], 0, (0,0,255), 2)

    vertice = len(aproximacao)
    if len(aproximacao) == 3:
        cv.drawContours(img, [contour], -1, (0, 255, 0), 3)  # Triângulo em verde
        cv.putText(img, 'Triangulo', tuple(aproximacao[0][0]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA)

    elif len(aproximacao) == 4:
        cv.drawContours(img, [contour], -1, (0, 255, 0), 3)  # Quadrilátero em verde
        cv.putText(img, 'Quadrilatero', tuple(aproximacao[0][0]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA)

   

cv.imshow('Result', img)
cv.waitKey(0)
cv.destroyAllWindows()