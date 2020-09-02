import cv2
import numpy as np
import processamento_de_imagens as pdi
import thresholding as threshold

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("Erro ao abrir o video")

firstFrame = None;

while cap.isOpened():
    (ret, frame) = cap.read()
    text = "Unoccupied"

    if not ret: #houve um erro ao capturar o frame
        break

    frame = pdi.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)

    #verificar se este frame e primeiro frame
    if firstFrame is None:
        firstFrame = blurred
        continue

    frameDelta = cv2.absdiff(firstFrame, blurred) #subtracao de fundo (estudar mais este conceito

    #binarizacao
    thresh, T = threshold.thresholdOtsu(frameDelta, False)
    #thresh = pdi.NOT(thresh)
    print(T)
    
    #dilatar imagem
    kernel = np.ones((3,3),np.uint8)
    frameDilate = cv2.dilate(thresh, kernel, iterations=1)
    
    #pegar contornos
    (cnts, _) = cv2.findContours(frameDilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, cnts, -1, (0, 255, 0), 2)

    #FALTA VERIFICAR SE ESTA IMAGEM TEM OU NAO UM DETERMINADO OBJETO
    '''

    #pegar um contorno de cada vez
    for c in cnts:
        if cv2.contourArea(c) < 100: #nao e o procurado
            continue

        
        (x, y, w, h) = cv2.boudingRect(c) #retorna (inicioX, inicio Y, largura, altura)
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
        text = "Occupied"
        '''
   
    temp = np.vstack([
        np.hstack([blurred, frameDelta]),
        np.hstack([thresh, frameDilate])
    ])
    
    pdi.show("Frame Inicial", firstFrame)
    pdi.show("Frame atual", frame)
    pdi.show("Frames apos processamento", temp)
    '''
    pdi.show("Frame atual com blurred", blurred)
    pdi.show("Frame com blurred e subtracao de fundo", frameDelta)
    pdi.show("Frame com blurred, substracao de fundo e Thresh Otsu", thresh)
    pdi.show("Frame dcom blurred, substracao de fundo e dilate", frameDilate)

    '''
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
