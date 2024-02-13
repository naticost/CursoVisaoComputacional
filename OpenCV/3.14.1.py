import cv2
import numpy as np

imagem_loading = cv2.imread('imagens/loading.jpg')  
if imagem_loading is None:
    print("Erro ao carregar a imagem.")
    exit()

altura, largura = imagem_loading.shape[:2]

angulo_rotacao = 0

while True:
    matriz_rotacao = cv2.getRotationMatrix2D((largura / 2, altura / 2), angulo_rotacao, 1)

    imagem_rotacionada = cv2.warpAffine(imagem_loading, matriz_rotacao, (largura, altura), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    cv2.imshow('Loading Animation', imagem_rotacionada)

    angulo_rotacao += 1

    cv2.waitKey(10)
    key = cv2.waitKey(1) & 0xFF
    if key != 255:
        break

cv2.destroyAllWindows()