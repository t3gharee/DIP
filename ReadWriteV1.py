# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:07:21 2020

@author: tghareeb
"""

import cv2, os

imgpath=(r"C:\Users\TGhareeb\OneDrive - DEI Associates\Documents\ELEC-tg-Surface\Documents\Documents\MASC"
         r"\00. Research Project\DIP material"
        r"\Python+Open CV\dataset\lena_color_512.tif")

img=cv2.imread(imgpath,1)  #  read the image in RGB - default mode
cv2.imshow('lenna', img)
k=cv2.waitKey(0)

outpath= (r"C:\Users\TGhareeb\OneDrive - DEI Associates\Documents\ELEC-tg-Surface\Documents\Documents\MASC"
    r"\00. Research Project\DIP material\Python+Open CV\OpenCVcodes\Output\\")

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite(outpath + 'lena_color_512_copy.jpg', img)
    cv2.destroyAllWindows()
    
# Check current working directory.
retval = os.getcwd()
print ("Current working directory     \n %s"   % retval)