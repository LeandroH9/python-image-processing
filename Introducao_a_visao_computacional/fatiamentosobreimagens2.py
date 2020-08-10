import numpy as np
import cv2

imagem = cv2.imread('entrada.jpg')

print(imagem.ndim) #a matriz tem 3 dimensoes -> são tres listas
# 1 - contem a matriz toda
# 2 - n listas (linhas)
# 3 - n listas (colunas)

vermelho = (0, 0, 255) #tupla que representa a cor vermelha
verde = (0, 255, 0) #tupla que representa a cor verde
azul = (255, 0, 0) #tupla que representa a cor azul


#cv2.line(img, coordenada inicial, coordenada final, cor da forma em tupla, espessura em px
cv2.line(imagem, (0,0), (100, 200), verde)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)

#cv2.rectangle(img, coordenada do canto superior esquerdo, coordenada do canto inferior direito, cor, espessura em px)
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1) #-1 -> preenche toda a forma

(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2) #desempacotamento e //->divisao inteira
for raio in range(0, 175, 15):
    #cv2.circle(img, coordenadas, raio, cor, espessura)
    cv2.circle(imagem, (X, Y), raio, vermelho) 


#exemplo de escrita sobre a iamgem. é possível escolher fonte, tamanho e posição.
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'OpenCV',(15,65), fonte,
2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)
