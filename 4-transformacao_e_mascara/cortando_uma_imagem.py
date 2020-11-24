
import cv2

imagem = cv2.imread('entrada.jpg')
recorte = imagem[100:200, 100:200] #técnica slicing é realizada

#recorte armazena uma imagem 'recortada' da imagem original, o termo em ingles é 'crop'
cv2.imshow("Recorte da imagem", recorte)
cv2.imwrite("recorte.jpg", recorte) #salva no disco


#temos uma imagem recortada da imagem original e salvada em um arquivo em disco


