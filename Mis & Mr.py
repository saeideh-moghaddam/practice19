import cv2
Ms = cv2.imread("Ms.jpg", 0)
Mr = cv2.imread("Mr.jpg", 0)

new_Ms = 255 - Ms[:, :]
new_Mr = 255 - Mr[:, :]

cv2.imwrite('new_Ms.jpg', new_Ms)
cv2.imwrite('new_Mr.jpg', new_Mr)
cv2.waitKey()