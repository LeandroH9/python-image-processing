
import cv2

imagem = cv2.imread('entrada.jpg')
(b, g, r) = imagem[0, 0] #a ordem é BGR e não RGB

#Use a função cv2.imshow () para exibir uma imagem em uma janela. A janela se ajusta automaticamente ao tamanho da imagem.
print('O pixel (0,0) tem as seguintes cores:')
print(f'azul: {b}')
print(f'verde: {g}')
print(f'vermelho: {r}')


#Use a função cv2.imshow () para exibir uma imagem em uma janela. A janela se ajusta automaticamente ao tamanho da imagem.
cv2.imshow('imagem', imagem)


cv2.waitKey(0) #recebe como argumento um tempo em milissegundos


cv2.destroyAllWindows()


