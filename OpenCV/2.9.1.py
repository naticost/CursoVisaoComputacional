import cv2 as cv 

robot = cv.imread('imagens/robot.jpg')
fit = cv.imread('imagens/fit.jpg')

img = cv.imread('imagens/fit.jpg', cv.IMREAD_GRAYSCALE)


limiar,img_bin = cv.threshold(img, 0, 255,cv.THRESH_BINARY + cv.THRESH_OTSU)

print(limiar)

fit_mask = cv.cvtColor(img_bin, cv.COLOR_GRAY2BGR)

fit_mask_inv = cv.bitwise_not(fit_mask)


img1 = cv.bitwise_and(robot, fit_mask)
img2 =cv.bitwise_and(fit, fit_mask_inv)

res = cv.add(img1, img2)

cv.imshow('Resultado', res)
cv.waitKey()