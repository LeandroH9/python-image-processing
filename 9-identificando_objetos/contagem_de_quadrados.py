import numpy as np
import cv2

image = np.zeros((500,500), dtype = "uint8")

for x in range(0, image.shape[1], 150):
    for y in range(0, image.shape[0], 200):
        cv2.rectangle(image, (x, y), (x + 50, y + 50), 255, -1)
        
cannyy = cv2.Canny(image, 20, 120)

(objetos, lx) = cv2.findContours(cannyy.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(image)
cv2.imshow("original", image)
cv2.imshow(f"imagem tem {len(objetos)} quadrados" , cannyy)

cv2.waitKey(0)
