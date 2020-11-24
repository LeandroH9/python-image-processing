import cv2

'''
Aqui, o algoritmo determina o limite de um pixel com base em uma pequena
região ao redor dele Portanto, obtemos limites diferentes para regiões diferentes da mesma imagem,
o que dá melhores resultados para imagens com iluminação variável

O adaptiveMethod decide como o valor limite é calculado:
-> cv.ADAPTIVE_THRESH_MEAN_C : O valor limite é a média da área do bairro menos a constante C .
-> cv.ADAPTIVE_THRESH_GAUSSIAN_C : O valor de limiar é uma soma de Gauss-ponderada dos valores de vizinhança menos a constante C .

O blockSize determina o tamanho da área da vizinhança e C é uma constante que é subtraída da média ou soma ponderada dos pixels da vizinhança.
'''

img = cv2.imread('entrada.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte

#cv2.adaptiveThreshold(imagem, valor maximo atribuido, como o valor limite é calculado, tipos de limite, tamanho da area de vizinhanca, constante que é subtraida da média) 
bin1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)

cv2.imshow("Imagem Original", img)
cv2.imshow("Binarizacao adaptativa da imagem pela media", bin1)
cv2.waitKey(0)
