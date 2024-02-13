import cv2
import numpy as np

def aplicar_erosao(imagem, quantidade_erosoes):
    kernel = np.ones((5, 5), np.uint8)

    for _ in range(quantidade_erosoes):
        imagem = cv2.erode(imagem, kernel, iterations=1)

    return imagem

imagem = cv2.imread('imagens/opencv.png')

if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    while True:
        cv2.imshow('Imagem', imagem)
        cv2.waitKey(0)

        quantidade_erosoes = int(input("Digite a quantidade de erosões 1-4:  (ou digite 0 para sair): "))

        if quantidade_erosoes == 0:
            break

        if 1 <= quantidade_erosoes <= 4:
            imagem = aplicar_erosao(imagem.copy(), quantidade_erosoes)
        else:
            print("Quantidade de erosões deve estar entre 1 e 4.")

cv2.destroyAllWindows()