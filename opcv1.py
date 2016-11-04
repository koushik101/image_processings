import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output7.avi',fourcc, 20.0, (640,480))
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #  retval,threshold = cv2.threshold(gray,155,255,cv2.THRESH_BINARY)
   # edges,contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    

    kernel = np.ones((16,16),np.float32)/256;
    smoothed = cv2.filter2D(frame,-1,kernel)
    fgmask = fgbg.apply(frame)
    edges = cv2.Canny(fgmask,100,200)

    out.write(edges)
    cv2.imshow('frame',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

