# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:20:39 2020

@author: tghareeb
"""
# Corner Detection
# Watch this https://pythonprogramming.net/corner-detection-python-opencv-tutorial/
import cv2, numpy as np
# import tlib.pyplot as plt


path=(r'C:\Users\TGhareeb\OneDrive - DEI Associates\Documents'
r'\ELEC-tg-Surface\Documents\Documents\MASC'
r'\00. Research Project\DIP material\Python+Open CV\dataset\\')

img=cv2.imread(path+'ruler.512.tiff')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.01, 10)
corners = np.int0(corners)

## Draw circles around detected corners
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,[255,0,255],-1)   # -1 means fill color
    
cv2.imshow('Corners',img)   

## Closing
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img),plt.show()

