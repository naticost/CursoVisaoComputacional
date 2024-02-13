import cv2
import numpy as np

def remover_ruidos(imagem, tamanho_kernel):
    imagem_filtrada = cv2.blur(imagem, (tamanho_kernel, tamanho_kernel))

    return imagem_filtrada

imagem_biometria = cv2.imread('imagens/biometria.JPG')

if imagem_biometria is None:
    print("Erro ao carregar a imagem.")
else:
    cv2.imshow('Imagem Original', imagem_biometria)
    cv2.waitKey(0)

    tamanho_kernel = 4

    imagem_sem_ruido = remover_ruidos(imagem_biometria, tamanho_kernel)

    cv2.imshow('Imagem Sem Ruídos', imagem_sem_ruido)
    cv2.waitKey(0)

    cv2.destroyAllWindows()