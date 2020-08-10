import cv2

imagem = cv2.imread('entrada.jpg')

#varrendo os pixels com laços de repetição (não muito performático)


#percorrendo os pixels e alterando seus respectivos valores para (255, 0, 0) -> azul
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (255, 0, 0)
cv2.imshow('Imagem modificada - toda azul', imagem)
cv2.waitKey (0)
cv2.destroyAllWindows ()


#percorrendo os pixels e alterando seus respectivos valores com relação a suas coordenadas
for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (x%256, y%256, x%256) 
cv2.imshow('Imagem modificada ', imagem)
cv2.waitKey (0)
cv2.destroyAllWindows ()

#alterando somente a cor verde com os valores de linha multipicado pela coluna
for x in range(0, imagem.shape[0], 1):
    for y in range(0, imagem.shape[1], 1):
        imagem[x, y] = (0, (x*y)%256, 0)
cv2.imshow("Imagem modificada - com verde", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows ()

#criando pontos amarelos na imagem, com uma distancia de 10 pixels entre as linhas e colunas
imagem = cv2.imread('entrada.jpg')
for x in range(0, imagem.shape[0], 10):
    for y in range(0, imagem.shape[1], 10):
        imagem[x: x + 5, y: y + 5] = (0, 255, 255) #quadrado amarelo de 5x5 pixels
cv2.imshow("Imagem modificada com pontos amarelos", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows ()











