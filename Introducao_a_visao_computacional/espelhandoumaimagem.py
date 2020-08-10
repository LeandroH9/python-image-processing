#para espelhar uma imagem, basta inverter suas linhas, suas colunas ou ambas
#inverter as linhas -> flip horizontal
#inverter as colunas -> flip vertical

import cv2
img = cv2.imread("entrada.jpg")
cv2.imshow("original", img)

#a função flip(imagem a inverter, operação de flip)
#OPERAÇÃO DE FLIP:
#0, para inverter a imagem em torno do eixo x (inversão vertical);
#> 0 para virar ao redor do eixo y (virar horizontal);
#<0 para virar os dois eixos.

flip_horizontal1 = img[:, ::-1]
flip_horizontal2 = cv2.flip(img, 1)
cv2.imshow("Flip Horizontal modelo 1", flip_horizontal1)
cv2.imshow("Flip Horizontal modelo 2", flip_horizontal2)

flip_vertical1 = img[::-1, :]
flip_vertical2 = cv2.flip(img, 0)

cv2.imshow("Flip Vertical modelo 1", flip_vertical1)
cv2.imshow("Flip Vertical modelo 2", flip_vertical2)

flip_hv1 = img[::-1, ::-1]
flip_hv2 = cv2.flip(img, -1)
cv2.imshow("Flip Horizontal e Vertical modelo 1", flip_hv1)
cv2.imshow("Flip Horizontal e Vertical modelo 2", flip_hv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

