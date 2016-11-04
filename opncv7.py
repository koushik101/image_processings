import cv2
import numpy as np
img = cv2.imread("bird.jpg")
height, width = img.shape[:2]
#rows,cols = img.shape
for i in range(5):
    img = cv2.pyrDown(img)

low_im = cv2.resize(img,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
cv2.imwrite("bird1.jpg",low_im)

for i in range(5):
    img = cv2.pyrUp(img)

upr_im = cv2.resize(img,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
cv2.imwrite("bird2.jpg",upr_im)
