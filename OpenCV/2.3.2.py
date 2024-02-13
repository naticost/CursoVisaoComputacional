import cv2

imagem = cv2.imread('imagens/fit.jpg')

ponto1 = (200,200)
ponto2 = (50,50)

mascara = cv2.imread('imagens/fit.jpg', 0)
mascara[ponto1[1]:ponto2[1],ponto1[0]:ponto2[0]] = 255

resultado = cv2.bitwise_and(imagem,imagem,mask=mascara)

cv2.imshow('Imagem Resultante', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()