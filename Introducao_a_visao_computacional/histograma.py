
'''
No Python, existe uma biblioteca muito famosa para criarmos gráficos,
é a Matplotlib.
Com ela, podemos montar diversos tipos de gráfico, como gráficos de barras, gráficos pizza, de dispersão, entre alguns outros.
'''
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("entrada.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #conveerte P&B
cv2.imshow("Imagem P&B", img)

#Função calHist para calcular o histograma da imagem
'''
cv2.calcHist (imagens, canais, máscara, histSize, intervalos [, hist [, acumular]])
imagens -> imagem a ser feito o calculo

canais -> Por exemplo, se a entrada for uma imagem em escala de cinza,
seu valor será [0]. Para imagem colorida, você pode passar [0], [1] ou [2] para
calcular o histograma dos canais azul, verde ou vermelho, respectivamente.

mascara -> mascarar: mascarar imagem. Para encontrar o histograma da imagem
completa, ele é fornecido como "NULL"

histSize -> representa nossa contagem de BIN. Precisa ser dado entre colchetes.
Para escala completa, passamos [256].

gamas -> esta é a nossa GAMA. Normalmente, é [0,256].
'''
h = cv2.calcHist([img], [0], None, [256], [0, 256])

#detalhando as informações no gráfico
plt.figure()
plt.title("Histograma P&B") #título do gráfico
plt.xlabel("Intensidade") #rotulo dos dados do eixo x (no eixo x temos as intensidades de 0 a 255)
plt.ylabel("Qtde de Pixels") #rotulo dos dados do eixo y (no eixo y temos as quantidade de pixels(
plt.plot(h) #basta falarmos para o pyplot plotar (plot) o nosso gráfico (recebe listas com valores)
plt.xlim([0, 256]) #do valor 0 ao valor 256 será mostrada no eixo x do grafico
plt.show()

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)

