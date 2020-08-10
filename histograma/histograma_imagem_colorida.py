from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('entrada.jpg')
cv2.imshow("Imagem Colorida", img)

#SEPARAR OS CANAIS
canais = cv2.split(img)
cores = ("b", "g", "r") 

print(canais)
print(cores)
cv2.waitKey(0)

plt.figure()
plt.title("Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
'''
Importante notar que a função "zip‟ cria uma lista de tuplas formada pelas união
das listas passadas e não tem nada a ver com um processo de compactação como
poderia se esperar.
'''

for (canal, cor) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    
plt.show()

    
