import cv2
import numpy as np

def on_mouse_click(event, x, y, flags, param):
    global pontos_cliques, contador_cliques, imagem_original

    if event == cv2.EVENT_LBUTTONDOWN:
        pontos_cliques.append([x, y])
        contador_cliques += 1

        if contador_cliques == 4:
            pontos_cliques = np.array(pontos_cliques, dtype=np.float32)
            ajustar_perspectiva()

def ajustar_perspectiva():
    global pontos_cliques, imagem_original

    pontos_destino = np.float32([[0, 0], [800, 0], [800, 600], [0, 600]])

    matriz_perspectiva = cv2.getPerspectiveTransform(pontos_cliques, pontos_destino)

    imagem_ajustada = cv2.warpPerspective(imagem_original.copy(), matriz_perspectiva, (800, 600))

    cv2.imshow('Imagem Ajustada', imagem_ajustada)

imagem_original = cv2.imread('imagens/galeria.jpg') 

if imagem_original is None:
    print("Erro ao carregar a imagem.")
    exit()

while True:
    imagem_visualizacao = imagem_original.copy()

    pontos_cliques = []
    contador_cliques = 0

    cv2.namedWindow('Imagem Original', cv2.WINDOW_NORMAL)

    cv2.setMouseCallback('Imagem Original', on_mouse_click)

    cv2.imshow('Imagem Original', imagem_visualizacao)

    key = cv2.waitKey(0) & 0xFF
    if key == 27:  # 27
        break
cv2.destroyAllWindows()