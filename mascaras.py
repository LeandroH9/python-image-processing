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
'''
mask - máscara de operação opcional, matriz de canal único de 8 bits,
que especifica os elementos da matriz de saída a serem alterados.
Se a região da imagem (em escala de cinza e depois mascarada) tiver cor preta
(com o valor 0), ela não será combinada (mesclando a região da primeira imagem
com a da segunda).
A operação de "E" será realizada apenas se a máscara [i] não for igual a zero,
caso contrário, o resultado de e a operação será zero
'''
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)
cv2.imshow("Mascara aplicada a imagem", img_com_mascara)
cv2.waitKey(0)

