import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    status,photo=cap.read()
    
    new=photo[200:270,300:360]
    new=cv2.resize(new,(200,200))
    photo[50:250,:200]=new
    cv2.imshow('photo',photo)
    if(cv2.waitKey(1)==13):
        break
cv2.destroyAllWindows()
