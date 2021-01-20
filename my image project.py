import pandas as pd
import cv2 
import numpy as np
cap=cv2.VideoCapture(0)
status,photo=cap.read()
cv2.imshow('cap',photo)
cv2.waitKey()
cap.release()

cap.release()
print(photo.shape)