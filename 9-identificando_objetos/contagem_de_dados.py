'''
1. Convertemos a imagem para tons de cinza.
2. Aplicamos blur para retirar o ruído e facilitar a identificação das bordas.
3. Aplicamos uma binarização na imagem resultando em pixels só brancos e pretos.
4. Aplicamos um detector de bordas para identificar os objetos.
5. Com as bordas identificadas, vamos contar os contornos externos para achar a
quantidade de dados presentes na imagem

'''

import numpy as np
import cv2
import mahotas
from matplotlib import pyplot as plt

#Função para facilitar a escrita nas imagens
def escreve(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    #escreve na img um determinado texto
    cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0, cv2.LINE_AA)

def histograma(img):
    h = cv2.calcHist([img], [0], None, [256], [0, 256]) #um array onde cada posição tem um valor associado (o número de pixel neste tom)
    plt.figure()
    plt.title("Histograma P&B") #título do gráfico
    plt.xlabel("Intensidade") #rotulo dos dados do eixo x (no eixo x temos as intensidades de 0 a 255)
    plt.ylabel("Qtde de Pixels") #rotulo dos dados do eixo y (no eixo y temos as quantidade de pixels(
    plt.plot(h) #basta falarmos para o pyplot plotar (plot) o nosso gráfico (recebe listas com valores)
    plt.xlim([0, 256]) #do valor 0 ao valor 256 será mostrada no eixo x do grafico
    plt.show()
                    

imgColorida = cv2.imread('dados.png') #carregando a imagem

#Se necessário o redimensioamento da imagem pode vir aqui

#passo 1: Convertemos a imagem para tons de cinza.
img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)


#passo 2: Aplicamos blur para retirar o ruído e facilitar a identificação das bordas.
suave = cv2.blur(img, (7, 7)) #suavização pela média de uma janela de 7x7

#print(suave)
#cv2.imshow("imagem suavizada", suave)


#passo 3: binarização resultando em pixels brancos e pretos
#Todos os pixels abaixo de T serão colocados em 0 e todos acima de T serão colocados em 255. Também pode-se aplicar o inverso
#Este métodos assume que há dois picos no histograma de tons de cinza da imagem, então ele tenta encontrar o melhor valor para separar estes picos, que seria nosso valor T

T = mahotas.thresholding.otsu(suave) #para adquirir nosso valor T
print(f'Otsu threshold: {T}')

bin = suave.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
#cv2.imshow("imagem binarizada", bin)
bin = cv2.bitwise_not(bin) #todos os pixels acima de 0 vao virar 0, e os iguais a 0 vao virar 255
#cv2.imshow("imagem binarizada com bitwise-not", bin)



#passo 4: Aplicamos um detector de bordas para identificar os objetos.
'''
O primeiro argumento é a imagem, e logo após é necessário dos valores, threshold1 e threshold2. Qualquer valor acima
de threshold2 será considerado um canto. Qualquer valor abaixo de threshold1 será considerado
um não-canto. Valores dentro da faixa são considerados cantos os não cantos de acordo com a
intensidade dos pixels,
'''
bordas = cv2.Canny(bin, 70, 150)
#cv2.imshow("aplicando o detector de bordas na imagem", bin)


#Passo 5: Identificação e contagem dos contornos da imagem

(objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#A variável lx (lixo) recebe dados que não são utilizados

escreve(img, "Imagem em tons de cinza", 0)
escreve(suave, "Suavizacao com Blur", 0)
escreve(bin, "Binarizacao com Metodo Otsu", 255)
escreve(bordas, "Detector de bordas Canny", 255)

print(objetos) #uma lista com todos as posicoes que fazem parte do contorno

temp = np.vstack([
    np.hstack([img, suave]),
    np.hstack([bin, bordas])
])


cv2.imshow("Quantidade de objetos: " + str(len(objetos)), temp)
cv2.waitKey(0)
imgC2 = imgColorida.copy()
cv2.imshow("Imagem Original", imgColorida)

cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)

escreve(imgC2, str(len(objetos))+" objetos encontrados!")
cv2.imshow("Resultado", imgC2)

cv2.waitKey(0)
