#uma máscara nada mais é que uma imagem onde cada pixel pode estar "ligado" ou "desligado"

import cv2
import numpy as np

img = cv2.imread("entrada.jpg")
cv2.imshow("original", img)

mascara = np.zeros(img.shape[:2], dtype = "uint8") #cria uma matriz com zeros do tamanho da imagem

(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2) #localizacao do centro da imagem

#cv2.circle(img, coordenadas, raio, cor, espessura)
cv2.circle(mascara, (cX, cY), 100, (255, 255, 255), -1)
cv2.imshow("Mascara ate agora", mascara)
cv2.waitKey(0)


img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)
cv2.imshow("Máscara aplicada a imagem", img_com_mascara)
cv2.waitKey(0)
