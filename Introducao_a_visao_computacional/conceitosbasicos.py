# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
imagem = cv2.imread('entrada.jpg')

print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)

#a funçao aguarda milissegundos especificados para qualquer eventos do teclado
#se for pressionado qualquer tecla nesse período, o programa não irá seguir
#Se 0 for passado, ele espera indefinidamente por um toque de tecla.
cv2.waitKey(0) #recebe como argumento um tempo em milissegundos e retorna qual tecla doi pressionada


#cv2.destroyAllWindows () simplesmente destrói todas as janelas que criamos. 
#cv2.destroyWindow () Se você deseja destruir qualquer janela específica, use esta função, onde passa o nome exato da janela como argumento
cv2.destroyAllWindows()

# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)

print('chegou aqui')
