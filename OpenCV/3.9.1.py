import cv2

def desenhar_circulo(imagem, centro, raio):
    centro = (int(centro[0]), int(centro[1]))
    raio = int(raio)

    imagem_desenhada = imagem.copy()
    cv2.circle(imagem_desenhada, centro, raio, (0, 255, 0), 2)  

    return imagem_desenhada

imagem = cv2.imread('imagens/andromeda.jpg')  
if imagem is None:
    print("Erro ao carregar a imagem.")
else:
    # Obter coordenadas (180, 90) e raio do círculo 67
    x = int(input("Digite a coordenada x do centro do círculo: "))
    y = int(input("Digite a coordenada y do centro do círculo: "))
    raio = int(input("Digite o raio do círculo: "))

    imagem_com_circulo = desenhar_circulo(imagem, (x, y), raio)

    cv2.imshow('Imagem com Círculo', imagem_com_circulo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()