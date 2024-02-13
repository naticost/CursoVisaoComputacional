import cv2 as cv
import numpy as np

img = cv.imread('imagens/fit.jpg')

img_nova = np.zeros_like(img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_canny = cv.Canny(img_gray, 100, 200)

linhas = cv.HoughLinesP(img_canny, 1, np.pi / 10, 20)

for linha in linhas:
    x1, y1, x2, y2 = linha[0]
    cv.line(img_nova, (x1, y1), (x2, y2), (255, 255, 255), 3)

  
    cv.imshow('Imagem com Linhas', img_nova)
    cv.waitKey(10)


cv.imshow('Imagem Original', img)
cv.waitKey(0)
cv.destroyAllWindows()