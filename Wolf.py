import cv2

image = cv2.imread("wolf.jpg", 0)
height, width = image.shape

for i in range(height):
    for j in range(width):
        if image[i, j] < 125:
            image[i, j] = 0
            
cv2.imwrite('new_wolf.jpg', image)
cv2.waitKey()