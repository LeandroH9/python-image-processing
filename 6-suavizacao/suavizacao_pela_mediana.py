

'''
 A mediana é semelhante à média, mas ela despreza os valores
muito altos ou muito baixos que podem distorcer o resultado. A mediana é o número que fica
examente no meio do intervalo.

A função utilizada é a cv2.medianBlur(img, 3) e o único argumento é o tamaho da
caixa ou janela usada
'''

import numpy as np
import cv2

img = cv2.imread('..\entrada.jpg')
img = img[::3, ::3] #diminui a imagem

suave = np.vstack([
    np.hstack([img, cv2.medianBlur(img, 3)]),
    np.hstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]),
    np.hstack([cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)])
])

cv2.imshow("imagem original e suavizada pela mediana", suave)
cv2.waitKey(0)
