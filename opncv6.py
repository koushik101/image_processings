import cv2
import numpy as np,sys
from scipy import sparse

A = cv2.imread('apple.jpg')
B = cv2.imread('orange.jpg')
height,width = A.shape[:2]
B = cv2.resize(B,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
 # generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
   G = cv2.pyrDown(gpA[i])
   G = cv2.resize(G,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
   gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(gpB[i])
    G = cv2.resize(G,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
    gpB.append(G)
    
# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    
    GE = cv2.pyrUp(gpA[i])
    GE = cv2.resize(GE,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)
 
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    
    GE = cv2.pyrUp(gpB[i])
    GE = cv2.resize(GE,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)
 
# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    la = cv2.resize(la,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
    lb = cv2.resize(lb,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    #ls = sparse.hstack((A[:,:cols/2],B[:,cols/2:]))
    LS.append(ls)
    
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
   
    ls_ = cv2.pyrUp(ls_,)
    ls_ = cv2.resize(ls_,(1*width, 1*height), interpolation = cv2.INTER_CUBIC)
    ls_ = cv2.add(ls_, LS[i])
 
# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))
#real = sparse.hstack((A[:,:cols/2],B[:,cols/2:]))
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
