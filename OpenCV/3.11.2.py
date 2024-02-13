import cv2
import numpy as np

def on_mouse_drag(event, x, y, flags, param):
    global desenhando

    if event == cv2.EVENT_LBUTTONDOWN:
        desenhando = True
        cv2.circle(imagem, (x, y), tamanho_pincel, (0, 0, 255), -1) 
    elif event == cv2.EVENT_MOUSEMOVE and desenhando:
        cv2.circle(imagem, (x, y), tamanho_pincel, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        desenhando = False

desenhando = False
tamanho_pincel = 10

imagem = cv2.imread('imagens/chuva.jpg') 
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

cv2.namedWindow('Desenho sobre Imagem', cv2.WINDOW_NORMAL)

cv2.setMouseCallback('Desenho sobre Imagem', on_mouse_drag)

while True:
    cv2.imshow('Desenho sobre Imagem', imagem)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()