

import cv2
import numpy as np

#FUNÇÕES UTEÍS
def infoImg(img):
    print(f'altura: {img.shape[0]}\nlargura: {img.shape[1]}\n')
    if isGrayScale(img) is False:
        print(f'Canais: {img.shape[2]}')

def readGrayScale(caminho):
    try:
        img = cv2.imread(caminho)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        print("\n Não foi possível abrir a imagem")
    else:
        return gray

def show(nomeImg, img):
    cv2.imshow(nomeImg, img)

def isGrayScale(img):
    if(len(img.shape)== 2):
        return True
    return False

#FUNCOES PARA CALCULAR GRADIENTE
def Laplacian(img):
    if isGrayScale(img) is False:
        return img
    lap = cv2.Laplacian(img, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    return lap

def sobelHorizontal(img):
    if isGrayScale(img) is False:
        return img
    sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobelX = np.uint8(np.absolute(sobelX))
    return sobelX

def sobelVertical(img):
    if isGrayScale(img) is False:
        return img
    sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobelY = np.uint8(np.absolute(sobelY))
    return sobelY

def Canny(img, threshold1, threshold2):
    if isGrayScale(img) is False:
        return img
    canny = cv2.Canny(img, threshold1, threshold2)
    return canny


def desenharContornos(img, contornos, index, cor, espessura):
    cv2.drawContours(img, contornos, index, cor, espesssura)
    return img
    
image = cv2.imread("entrada2.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5,5), 0)
show("original suavizada", image)

canny = Canny(blurred, 30, 150)
show("imagem com CANNY", canny)

(cnts, lx) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts -> um array com todas as posições de canto


imagemColorida = image.copy()
cv2.drawContours(imagemColorida, cnts, -1, (255,0,0), 2)
show("imagem com contornos", imagemColorida)

'''
sobelX = sobelHorizontal(image)
sobelY = sobelVertical(image)

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
show("horizontal sobel", sobelX)
show("vertical sobel", sobelY)
show("combinacao sobel", sobelCombined)



lap = Laplacian(image, cv2.CV_64F)
show("Laplacian", lap)
'''
cv2.waitKey(0)
