import cv2

imagem_original = cv2.imread('imagens/andromeda.jpg')

if imagem_original is None:
    print("Erro ao carregar a imagem.")
else:
    cv2.namedWindow('Imagens Resultantes', cv2.WINDOW_NORMAL)

    cv2.imshow('Imagens Resultantes', imagem_original)
    cv2.waitKey(0)

    for i in range(1, 101):
        fator_reducao = 0.9  
        imagem_redimensionada = cv2.resize(imagem_original, None, fx=fator_reducao, fy=fator_reducao, interpolation=cv2.INTER_NEAREST)

        imagem_restaurada = cv2.resize(imagem_redimensionada, (imagem_original.shape[1], imagem_original.shape[0]), interpolation=cv2.INTER_NEAREST)

        cv2.imshow('Imagens Resultantes', imagem_restaurada)
        cv2.waitKey(0)

        imagem_original = imagem_restaurada.copy()

    cv2.destroyAllWindows()