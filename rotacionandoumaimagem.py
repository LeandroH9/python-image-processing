

import cv2
img = cv2.imread('entrada.jpg')
(alt, lar) = img.shape[:2] #captura altura e largura (0, 1)
centro = (lar // 2, alt // 2)  #pega a posicao do pixel no centro

M = cv2.getRotationMatrix2D(centro, 90, 1.0) #90 graus
img_rotacionada = cv2.warpAffine(img, M, (lar, alt))

cv2.imshow("Imagem rotacionada em 30 graus", img_rotacionada)
cv2.waitKey(0)
