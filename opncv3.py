import numpy as np
import cv2 

img = cv2.imread('city.jpg')
dst = cv2.fastNlMeansDenoisingColored(img,None,8,8,12,15)

cv2.imshow('img',img)

cv2.imshow('dst',dst)

