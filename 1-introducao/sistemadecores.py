

import cv2
img = cv2.imread('minha_foto.jpeg')
cv2.imshow("original", img)

'''
cv2.cvtColor()O método é usado para converter
uma imagem de um espaço de cores para outro.
cv2.cvtColor(imagem cujo deve ser alterado, código de conversao) -> retorna uma imagem
'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Gray -> preto e branco -> tons de cinza
cv2.imshow("Gray", gray)
cv2.imwrite("minha_foto_bp.png", gray)
cv2.imwrite("minha_foto.png", img)

'''
Usando o espaço de cores HSV.
O espaço de cores HSV é usado principalmente para rastreamento de objetos.

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
'''
cv2.waitKey(0)
