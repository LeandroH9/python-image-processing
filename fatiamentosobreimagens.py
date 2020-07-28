
import cv2

image = cv2.imread("entrada.jpg")

image[0, 0] = (255, 255, 0)
print(image[0,0])
print(image)

#CRIA UM RETANGULO AZUL DE ALTURA ENTRE 30 E 50 E POR TODA A LARGURA DA IMAGEM
image[30:50, :] = (255, 0, 0);#slicing -> altera vários pixels da imagem de uma vez só

#CRIA UM QUADRADO VERMELHO
image[100:150, 50:100] = (0, 0, 255)

#CRIA UMA RETANGULO AMARELO POR TODA A ALTURA DA IMAGEM
image[:, 200:220] = (0, 255, 255)

#CRIA UM RETANGULO VERDE DA LINHA 150 A 300 NAS COLUNAS 250 A 350
image[150:300, 250:350] = (0, 255, 0)

#CRIA UM QUADRADO CIANO DA LINHA 50 A 150 NAS COLUNAS 300 A 400
image[300:400, 50:150] = (255, 255, 0)

#CRIA UM QUADRADO BRANCO
image[250:350, 300:400] = (255, 255, 255)

#CRIA UM QUADRADO PRETO
image[70: 100, 300: 450] = (0,0,0)

cv2.imshow("Imagem alterada", image) #exibe a imagem após a execução do código acima com os retangulos coloridos incluídos pela técnica "slicing"
cv2.waitKey(0);
cv2.destroyAllWindows();
