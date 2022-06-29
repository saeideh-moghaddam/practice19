import cv2
import numpy as np

image = np.arange(0, 640000, 1, np.uint8)
img = np.reshape(image, (800, 800))
width,height = img.shape

for i in range(0,width,100):
    for j in range(0,height,100):
        if ((i+j)/4)%2==0:
            img[i:i+100,j:j+100]=0
        else:
            img[i:i+100,j:j+100]=255

cv2.imshow("chess_board.jpg",img)
cv2.waitKey()