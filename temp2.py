# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:07:57 2020

@author: yangy
"""

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\yangy\Desktop\0001.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([40, 40,40])
upper_range = np.array([70, 255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow("Image", img)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()