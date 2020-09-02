import numpy as np
import cv2

#FUNÇÕES UTEÍS
def infoImg(img):
    print(f'altura: {img.shape[0]}\nlargura: {img.shape[1]}\n')
    if isGrayScale(img) is False:
        print(f'Canais: {img.shape[2]}')

def read(caminho):
    try:
        image = cv2.imread(caminho)
    except:
        print("\n Não foi possível abrir a imagem")
    else:
        return image

def show(nomeImg, img):
    cv2.imshow(nomeImg, img)

def isGrayScale(img):
    if(len(img.shape)== 2):
        return True
    return False

#FUNÇÕES DE MANIPULAÇÃO
def translate(img, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]]) #[[1,0,Tx], [0,1,Ty]]
    print(M)
    shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0])) #(largura, altura)

    return shifted

def rotate(img, angle, center = None, scale = 1.0):
    (h, w) = img.shape[:2]

    if center is None:
        center = (w // 2, h // 2) #pega a posicao do pixel no centro
        
    M = cv2.getRotationMatrix2D(center, angle, scale)
    print(M)
    rotated = cv2.warpAffine(img, M, (w, h))

    return rotated

def resize(img, height = None, width = None, inter = cv2.INTER_AREA):
    (h, w) = img.shape[:2]
    
    if width is None and height is None:
        return image
    elif width is None:
        r = height / float(h) 
        dimensao = (int(w * r), height)
    elif height is None:
        r = width / float(w)
        dimensao = (width, int(h * r))
    else:
        dimensao = (width, height)
        
    resized = cv2.resize(img, dimensao, interpolation = inter)
        
    return resized
    
def flip(img, operacao):
    flipped = cv2.flip(img, operacao)
    return flipped

def crop(img, startX, finalX, startY, finalY):
    cropped = img[startY:finalY, startX:finalX]
    return cropped


#FUNÇÕES ARITMÉTICAS
def add(img, valor):
    if(valor > 255 or valor < 0):
        return img
    M = np.ones(img.shape, dtype = "uint8") * valor #cria uma matriz com elementos iguais a "valor"
    added = cv2.add(img, M)
    return added;

def subtract(img, valor):
    if(valor > 255 or valor < 0):
        return img
    M = np.ones(img.shape, dtype = "uint8") * valor #cria uma matriz com elementos iguais a "valor"
    subtracted = cv2.subtract(img, M)
    return subtracted


#OPERAÇÕES BITWISE 

def AND(img1, img2):
    if(isGrayScale(img1) and IsGrayScale(img2)):
        BitAnd = cv2.bitwise_and(img1, img2)
        return BitAnd
    return None

def OR(img1, img2):
    if(isGrayScale(img1) and IsGrayScale(img2)):
        BitOr = cv2.bitwise_or(img1, img2)
        return BitOr
    return None
    
def XOR(img1, img2):
    if(isGrayScale(img1) and IsGrayScale(img2)):
        BitXor = cv2.bitwise_xor(img1, img2)
        return BitXor
    return None
    

def NOT(img1):
    if isGrayScale(img1):
        BitNot = cv2.bitwise_not(img1)
        return BitNot
    return None

def maskRetangle(img, w, h): #figura 0 -> quadrado, figura 1 -> circulo
    (cX, cY) = img.shape[1] // 2, img.shape[0] // 2
    w, h = w // 2, h // 2
    mask = np.zeros(img.shape[:2], dtype = "uint8")
    cv2.rectangle(mask, (cX - w, cY - h), (cX + w, cY + h), 255, -1)
    masked = cv2.bitwise_and(img, img, mask = mask)

    return masked

#SEPARACAO e UNIAO DE CANAIS
def split(img):
    if isGrayScale(img) is False:
        (B, G, R) = cv2.split(img)
        return (B, G, R)
    return img

def merge(img, B = None, G = None, R = None):
    zeros = np.zeros(img.shape[:2], dtype = "uint8")
    if B is None:
        B = zeros.copy()
    if G is None:
        G = zeros.copy()
    if R is None:
        R = zeros.copy()
    mergeed = cv2.merge([B, G, R])
    return mergeed
        
'''
image = read("entrada2.jpg")
show("original", image)
infoImg(image)

'''
