
import cv2
import numpy as np

#no open cv é permitido separar e vizualizar cada canal de cor individualmente

img = cv2.imread("entrada.jpg")

'''
A função „split‟ faz o trabalho duro separando os canais.
Assim podemos exibí-los em tons de cinza conforme mostra a imagem abaixo:
'''
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)


cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)

cv2.waitKey(0) 
cv2.destroyAllWindows()
'''
Também é possível alterar individualmente as Numpy Arrays que formam cada canal
e depois juntá-las para criar novamente a imagem. Para isso use o comando:
'''
resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])
cv2.imshow("Resultado na mesclagem das cores", resultado)

cv2.waitKey(0) 
cv2.destroyAllWindows()

zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv2.imshow("preta", zeros)

#zera as outras cores, e deixa somente os tons de vermelho
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))

cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))

cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))

cv2.imshow("Canal Verde e Vermelho", cv2.merge([zeros, canalVerde, canalVermelho]))

cv2.imshow("original", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
