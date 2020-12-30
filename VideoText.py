# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:56:16 2020

@author: tghareeb
"""

import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 3000)   # Change width is height is not available for laptop webcam
#cap.set(4, 3000)
#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_SIMPLEX
       text = '(Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))+')'
       datet = str(datetime.datetime.now())
       
       frame = cv2.putText(frame, text, (10, 50), font, 0.5,
                           (0, 255, 255), 1, cv2.LINE_AA)
      
       frame = cv2.putText(frame, datet, (10, 80), font, 0.5,
                           (0, 255, 0), 1, cv2.LINE_AA)
      
       frame = cv2.resize(frame,(960, 720), interpolation = cv2.INTER_CUBIC)

       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == 27:
       # if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()