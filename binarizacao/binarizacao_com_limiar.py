'''
Aqui, o assunto é direto. Para cada pixel, o mesmo valor limite é aplicado.
Se o valor do pixel for menor que o limite,
ele será definido como 0, caso contrário, será definido como um valor máximo.

A função cv.threshold é usada para aplicar o limite.
-> primeiro argumento é a imagem de origem, que deve ser uma imagem em tons de cinza .
-> O segundo argumento é o valor limite que é usado para classificar os
valores de pixel.
-> O terceiro argumento é o valor máximo atribuído aos valores de pixel que
excedem o limite.
O OpenCV fornece diferentes tipos de limite, que são fornecidos pelo quarto parâmetro da função.
Limiar básico conforme descrito acima é feito usando o tipo cv.THRESH_BINARY


O método retorna duas saídas. O primeiro é o limite que foi usado e a segunda saída é a imagem limite .
'''

import cv2
import numpy as np

img = cv2.imread('entrada.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(T, bin) = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY_INV)




print(T)
cv2.imshow("Imagem original", img)
cv2.imshow("Binarizacao da imagem Binaria", bin)
cv2.imshow("Binarizacao da imagem Binaria Invertida", binI)
cv2.waitKey(0)
