#a funcao para reduzir ou aumentar o tamanho de uma imagem é chamada 'resize'

import numpy as np
import cv2

img = cv2.imread('entrada.jpg')
cv2.imshow("Original", img)

proporcao = 100.0 / img.shape[1] #para não distorcer a imagem
tamanho_novo = (100, int(img.shape[0] * proporcao)) #uma tupla que vai armazenar a largura e altura da iamgem

img_redimensionada = cv2.resize(img, tamanho_novo, interpolation = cv2.INTER_AREA)
#cv2.INTER_AREA que é uma especificação do cálculo matemático para redimensionar a imagem

cv2.imshow("imagem redimensionada", img_redimensionada)
cv2.waitKey(0)

#Outra meneira de redimensionar a imagem para tamanhos menores ou maiores é utilizando a técnica de „slicing‟.
img_redimensionada = img[::2, ::2]
#O código basicamente refaz a imagem interpolando linhas e colunas, ou seja, pega a
#primeira linha, ignora a segunda, depois pega a terceira linha, ignora a quarta, e assim por
#diante. O mesmo é feito com as colunas.
cv2.imshow("imagem redimensionada", img_redimensionada)
cv2.waitKey(0)
