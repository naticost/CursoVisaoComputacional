import cv2

image = cv2.imread('imagens/estrada.jpg', cv2.IMREAD_GRAYSCALE)

threshold_1 = 50
threshold_2 = 150

edges = cv2.Canny(image, threshold_1, threshold_2)

cv2.imshow('Original Image', image)
cv2.imshow('Edges ( Canny)', edges)
cv2.waitKey()
cv2.destroyAllWindows()