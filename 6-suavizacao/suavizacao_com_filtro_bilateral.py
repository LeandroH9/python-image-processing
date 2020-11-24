'''
Este método é mais lento para calcular que os anteriores mas como vantagem
apresenta a preservação de bordas e garante que o ruído seja removido

Para realizar essa tarefa, além de um filtro gaussiano do espaço ao redor do pixel 
34
também é utilizado outro cálculo com outro filtro gaussiano que leva em conta a diferença de
intensidade entre os pixels, dessa forma, como resultado temos uma maior manutenção das
bordas das imagem.

'''

import cv2
import numpy as np

img = cv2.imread('../entrada.jpg')
img = img[::2,::2] # Diminui a imagem
suave = np.vstack([
    np.hstack([img, cv2.bilateralFilter(img, 3, 21, 21)]),
    np.hstack([cv2.bilateralFilter(img, 5, 35, 35), cv2.bilateralFilter(img, 7, 49, 49)]),
    np.hstack([cv2.bilateralFilter(img, 9, 63, 63), cv2.bilateralFilter(img, 11, 77, 77)])
])

cv2.imshow("Suavizacao com filtro Bilateral", resultado)
cv2.waitKey(0)

