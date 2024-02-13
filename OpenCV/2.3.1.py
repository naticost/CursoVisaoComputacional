import cv2 as cv

imagem = cv.imread('imagens/fit.jpg')
altura, largura, _ = imagem.shape

def obterValores_BGR(x, y):
    if 180 <= x < largura and 90 <= y < altura:

        try:
            b, g, r =imagem [y,x]
            print(f'Cordenadas ({x}, {y}): B={b}, G={g}, R={r}')
        except IndexError:
            print('Coordenadas inválidas')

    else:
        print('Coordenadas fora dos limites da imagem.')

try:        
    coord_x = int(input('Digite as coordenadas x: '))
    coord_y = int(input('Digite as coordenadas y: '))
    obterValores_BGR(coord_x, coord_y)

except ValueError:
    obterValores_BGR(coord_x, coord_y)