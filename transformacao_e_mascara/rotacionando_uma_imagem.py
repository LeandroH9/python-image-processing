

import cv2
img = cv2.imread('..\entrada.jpg')
print(img.shape)

(alt, lar) = img.shape[:2] #captura altura e largura (0, 1)
centro = (lar // 2, alt // 2)  #pega a posicao do pixel no centro

#M -> matriz de deslocamento
M = cv2.getRotationMatrix2D(centro, 30, 1.0) #90 graus

'''
warpAffine -> Esse método espera o objeto de imagem que será transladado
(primeiro parâmetro informado na linha 3 do código abaixo),
uma matriz de deslocamento (segundo parâmetro) e as dimensões
da imagem (terceiro parâmetro sendo passado como um array)
'''
img_rotacionada = cv2.warpAffine(img, M, (lar, alt))

cv2.imshow("Imagem rotacionada em 30 graus", img_rotacionada)
cv2.waitKey(0)



