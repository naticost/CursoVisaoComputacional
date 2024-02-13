import cv2

imagem = cv2.imread('imagens/celularRuido.jpg')

imagemGray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

imagemSemRuido = cv2.medianBlur(imagemGray, 5)

cv2.imshow('ImagemOriginal', imagem)
cv2.imshow('Imagem Sem Ruido', imagemSemRuido)
cv2.waitKey()
cv2.destroyAllWindows()