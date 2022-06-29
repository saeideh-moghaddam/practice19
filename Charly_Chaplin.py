import cv2
img = cv2.imread('charli_chaplin.jpg', 0)
height, width = img.shape

for i in range(200, 0, -1):
    for j in range(200, 0, -1):
        if i + j > 150 and i + j < 180 :
            img[i, j] = 0

show_image = cv2.resize(img, (width // 2, height // 2))
cv2.imshow(':(', show_image)
cv2.imwrite('charli_chaplin.jpg', img)
cv2.waitKey()