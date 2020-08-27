#OPERAÇÕES BITWISE - utilizados quando utilizamos uma escala de tons de cinza
# se 0 -> bit desligado, se > 0 -> acesso

#E(AND) -> sera verdadeiro se ambos os pixels forem maiores que zero
#OU(OR) -> sera verdadeiro se um ou outro pixel for maior que zero
#OU-EXCLUSIVO (XOR): Será verdadeiro se e somente se os dois pixels forem
#maiores que zero, mas não se os dois forem ao mesmo tempo.
#NÃO (NOT): Irá inverter os valores de “acesso” e “desligado” dos pixels.

import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype = "uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

print(rectangle.shape[0])

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)



