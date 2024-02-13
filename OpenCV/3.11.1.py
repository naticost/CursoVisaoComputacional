import cv2

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
    
        cv2.rectangle(imagem, (x - 1, y - 1), (x + 1, y + 1), (0, 0, 0), 2) 
        cv2.imshow('Imagem com Quadrado', imagem)

imagem = cv2.imread('imagens/pessoas.jpg')

if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    cv2.namedWindow('Imagem com Quadrado', cv2.WINDOW_NORMAL)

    cv2.setMouseCallback('Imagem com Quadrado', on_mouse_click)

    while True:
        cv2.imshow('Imagem com Quadrado', imagem)

        key = cv2.waitKey(1) & 0xFF
        if key == 27: 
            break

    cv2.destroyAllWindows()