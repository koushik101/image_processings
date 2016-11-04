import numpy as np
import cv2
img = cv2.imread('talkie.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold = cv2.threshold(gray,155,255,cv2.THRESH_BINARY)
res2,contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
