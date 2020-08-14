
'''
A suavisação da imagem (do inglês Smoothing), também chamada de „blur‟ ou
„blurring‟ que podemos traduzir para “borrão”, é um efeito que podemos notar nas fotografias
fora de foco ou desfocadas onde tudo fica embasado.

 Esse efeito é muito útil quando utilizamos
algoritmos de identificação de objetos em imagens pois os processos de detecção de bordas
por exemplo, funcionam melhor depois de aplicar uma suavização na imagem.

'''

'''
SUAVIZACAO PELA MEDIA
Neste caso é criada uma “caixa de pixels” para envolver o pixel em questão e calcular
seu novo valor. O novo valor do pixel será a média simples dos valores dos pixels dentro da
caixa, ou seja, dos pixels da vizinhança. Alguns autores chamam esta caixa de janela de
cálculo ou kernel (do inglês núcleo)

OS PARAMETROS
Os parâmetros são a imagem a ser suavizada e a janela de
suavização. Colocarmos números impars para gerar as caixas de cálculo pois dessa forma não
existe dúvida sobre onde estará o pixel central que terá seu valor atualizado
'''

import cv2
import numpy as np

img = cv2.imread("..\entrada.jpg")
img = img[::3, ::3] #diminui a imagem

horizontal = np.hstack([img, cv2.blur(img, (3,3))]);
vertical = np.vstack([img, cv2.blur(img, (5,5))]);
cv2.imshow("testando hstack", horizontal)
cv2.imshow("testando vstack", vertical)
cv2.waitKey(0)

'''
vstack (pilha vertical) e hstack (pilha horizontal) para
juntar as imagens em uma única imagem final mostrando desde a imagem original e seguinte
com caixas de calculo de 3x3, 5x5, 7x7, 9x9 e 11x11.
'''

suave = np.vstack([
 np.hstack([img, cv2.blur(img, (3, 3))]),
 np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, ( 7, 7))]),
 np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))]),
 ])


cv2.imshow("Imagens suavisadas (Blur)", suave)
cv2.waitKey(0)
'''              
 Perceba que conforme aumenta a caixa maior é o efeito de
borrão (blur) na imagem. '''
