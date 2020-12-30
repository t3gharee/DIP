# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:10:17 2020

@author: tghareeb
"""

# object tracking by its color
# https://youtu.be/WiT0Pz_M2DQ


import cv2, numpy as np
def main():
    
    cap=cv2.VideoCapture(0)  # capture video from first camera
    
    if cap.isOpened():
        ret , frame=cap.read()
    else:
        ret = False
    
    
    while ret:
        ret, frame=cap.read()
        
        # cv2.imshow('original video test', frame)
        
        # start color detection
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # covert to HSV color space or easy color detection
        low_blue=np.array([100,50,50])  # blue color range detection, this is dark blue
        high_blue=np.array([140,255,255]) # light blue
        blue_mask=cv2.inRange(hsv,low_blue,high_blue) # return bianry matrix highlighting the seelcted color range 
        cv2.imshow('original video HSV', hsv)
        cv2.imshow('Blue Mask',  blue_mask)
        if cv2.waitKey(1) == 27:     # eixt on Esc.
            break
        
    cap.release()
    cv2.destroyAllWindows()  
    
        
if __name__ == "__main__" :
    main()
