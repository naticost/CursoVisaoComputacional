import cv2

imagem = cv2.imread('imagens/opencv.png')

pixel_vermelho = [0, 0, 255]

pixel_encontrado = False

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if(imagem[i,j] == pixel_vermelho).all():
            pixel_encontrado = True
            coordenadas = (i,j)
            break
    if pixel_encontrado:
        break

cv2.imshow('Imagem Original',imagem)


if pixel_encontrado:
    print(f'Pixel Vermelho encontrado nas coordenadas: {coordenadas}')
else:
    print("Sem vermelho")

cv2.waitKey(0)
cv2.destroyAllWindows()