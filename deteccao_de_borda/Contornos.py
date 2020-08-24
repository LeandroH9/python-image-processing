'''
tem-se uma tupla com três retornos, a imagem com os contornos detectados, os contornos em si e a hierarquia de contornos
O primeiro argumento é a imagem.
Importante saber que, este processo irá destruir a imagem, deixando apenas os contornos.
O segundo argumento é o tipo de contorno procurado. Usou-se cv2.RETR_EXTERNAL para
selecionar apenas os contornos mais de fora.
O último argumento é como aproxima-se o contorno. Foi usado
cv2.CHAIN_APPROX_SIMPLE para um melhor contorno.
'''
'''
Os contornos podem ser explicados simplesmente como uma curva que une todos os pontos contínuos (ao longo da fronteira), tendo a mesma cor ou intensidade.
Os contornos são uma ferramenta útil para análise de formas e detecção e reconhecimento de objetos.

Para melhor precisão, use imagens binárias. Portanto, antes de encontrar contornos, aplique a detecção de limite ou de borda astuta.
Desde o OpenCV 3.2, findContours () não modifica mais a imagem de origem.
No OpenCV, encontrar contornos é como encontrar um objeto branco em um fundo preto. Portanto, lembre-se de que o objeto a ser encontrado deve ser branco e o fundo preto.
'''

import numpy as np
import cv2 as cv
im = cv.imread('test.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
