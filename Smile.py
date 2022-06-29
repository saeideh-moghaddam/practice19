import cv2

image = cv2.imread("upset.jpg")
height, width, channel = image.shape

image[:, :] = image[height::-1, width::-1]
show_img = cv2.resize(image, (width // 2, height// 2))

cv2.imshow("Let's smile", show_img)
cv2.imwrite("smile.jpg", image)
cv2.waitKey()