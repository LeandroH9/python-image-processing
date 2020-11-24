
'''
Na limitação global, usamos um valor escolhido arbitrariamente como limite.
Em contraste, o método de Otsu evita ter que escolher um valor e o determina
automaticamente

Da mesma forma, o método de Otsu determina um valor de limite global ideal a
partir do histograma da imagem.

Para fazer isso, a função cv.threshold () é usada, onde cv.THRESH_OTSU é
passado como um sinalizador extra. O valor limite pode ser escolhido
arbitrariamente. O algoritmo então encontra o valor limite ideal que é
retornado como a primeira saída

'''


import cv2 
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('entrada.jpg',0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('global', ret1)
print(th1)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otsu', ret2)


''' Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imread('gaussian + otsu' , th3)
'''

cv2.waitKey(0)
