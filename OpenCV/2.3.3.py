import cv2

image_escala_cinza = cv2.imread('imagens/pingpong.JPG', cv2.IMREAD_GRAYSCALE)

limite_superior = 35
limite_inferior = 20

_, imagem_resultante = cv2.threshold(image_escala_cinza, limite_inferior, limite_superior,cv2.THRESH_TOZERO)
_, imagem_resultante = cv2.threshold(imagem_resultante, limite_superior,limite_superior,cv2.THRESH_TRUNC)


cv2.imshow('Imagem Resultante', imagem_resultante)
cv2.waitKey(0)
cv2.destroyAllWindows()