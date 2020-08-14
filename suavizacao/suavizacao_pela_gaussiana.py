'''
Ao invés do filtro de caixa é utilizado um kernel gaussiano. Isso é calculado através da
função cv2.GaussianBlur(). A função exige a especificação de uma largura e altura com
números impares e também, opcionalmente, é possível especificar a quantidade de desvios
padrão no eixo X e Y (horizontal e vertical). '''

import cv2
import numpy as np

img = cv2.imread('..\entrada.jpg')
img = img[::2, ::2] # diminui a imagem

'''
 A função exige a especificação de uma largura e altura com
números impares e também, opcionalmente, é possível especificar a quantidade de desvios
padrão no eixo X e Y (horizontal e vertical).
'''

suave = np.vstack([
    np.hstack([img, cv2.GaussianBlur(img, ( 3, 3), 0)]),
    np.hstack([cv2.GaussianBlur(img, ( 5, 5), 0), cv2.GaussianBlur(img, ( 7, 7), 0)]),
    np.hstack([cv2.GaussianBlur(img, ( 9, 9), 0), cv2.GaussianBlur(img, (11, 11), 0)]),
 ])
cv2.imshow("Imagem original e suavisadas pelo filtro Gaussiano", suave)
cv2.waitKey(0)

'''
Veja nas imagens como o filtro de kernel gaussiano gera menos borrão na imagem
mas também gera um efeito mais natural e reduz o ruído na imagem.
'''
