import cv2

cap = cv2.VideoCapture(0)
'''
cap.read()retorna um bool (verdadeiro / falso). Se o quadro for lido corretamente, será True.
Portanto, você pode verificar o final do vídeo verificando este valor de retorno
'''
if cap.isOpened() is True:
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        (b, g, r) = frame[200, 200]
        frame[198: 202, 198:202] = (0, 0, 255)
        frame[10:90, 10:90] = (b, g, r)

        cv2.imshow( 'Frame', frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
