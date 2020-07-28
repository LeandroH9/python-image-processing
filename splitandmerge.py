import cv2
import numpy as np

img = cv2.imread("entrada.jpg")

zeros = np.zeros(img.shape[:2], dtype="uint8")
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

cv2.imshow("Preta", zeros)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
print(canalVermelho)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagemVermelha = cv2.merge([zeros, zeros, canalVermelho])
cv2.imshow("Vermelho", imagemVermelha)


print(imagemVermelha)



