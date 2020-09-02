
import numpy as np
import cv2
import mahotas
import processamento_de_imagens as pdi


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

#MÉTODOS DE THRESHOLD
def thresholdBinary(img, T):
    if isGrayScale(img) is False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (T, thresh) = cv2.threshold(img, T, 255, cv2.THRESH_BINARY)
    return (T, thresh)

def thresholdBinaryInv(img, T):
    if isGrayScale(img) is False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (T, threshInv) = cv2.threshold(img, T, 255, cv2.THRESH_BINARY_INV)
    return (T, threshInv)

def thresholdAdaptiveMean(img, inverse, tamVizinhanca, C):
    if isGrayScale(img) is False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if inverse is True:
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, tamVizinhanca, C)
    else:
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, tamVizinhanca, C)

    return thresh

def thresholdAdaptiveGaussian(img, inverse, tamVizinhanca, C = 0):
    if isGrayScale(img) is False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if inverse is True:
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, tamVizinhanca, C)
    else:
        thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, tamVizinhanca, C)
    return thresh

def thresholdOtsu(img, inverse):
    if isGrayScale(img) is False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    T = mahotas.thresholding.otsu(img)
    thresh = img.copy()
    thresh[thresh > T] = 255
    thresh[thresh < 255] = 0
    
    if inverse is True:
        thresh = cv2.bitwise_not(thresh)
        
    return (thresh, T)
    
def thresholdRiddlerCalvard(img, inverse):
    if isGrayScale(img) is False:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    T = mahotas.thresholding.rc(img)
    thresh = img.copy()
    thresh[thresh > T] = 255
    thresh[thresh < 255] = 0
    
    if inverse is True:
        thresh = pdi.NOT(thresh)
        
    return (thresh, T)

'''
image = readGrayScale("entrada2.jpg")
show("original", image)
infoImg(image)

burred = cv2.GaussianBlur(image, (5,5), 0) #Aplicar esse método ajuda a remover alguns cantos de frequência alta na imagem
show("imagem suavizada", burred)


threshOtsu, T = thresholdOtsu(burred, False)
print(T)
threshRC, T = thresholdRiddlerCalvard(burred, True)
print(T)
show("imagem threshold otsu", threshOtsu)
show("imagem threshold rc", threshRC)



threshMean = thresholdAdaptiveMean(burred, False, 11, 4)
threshGaussian = thresholdAdaptiveGaussian(burred, False, 11, 3)
show("imagem binary mean", threshMean)
show("imagem binary gaussian", threshGaussian)



T1, thresh = thresholdBinary(burred, 155)
T2, threshInv = thresholdBinaryInv(burred, 155)
show("imagem binary", thresh)
show("imagem binary inv", threshInv)
'''

