# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:24:05 2020

@author: yangy
"""

# Improting Image class from PIL module 
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\yangy\Desktop\0001.jpg")

height, width = img.shape[:2]
start_height = int(height * .5)
end_height, end_width = int(height * .88), int(width * .5)
cropped_img = img[start_height:end_height , 0:end_width]

hsv = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)

lower_range = np.array([40, 40,40])
upper_range = np.array([70, 255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", cropped_img)
cv2.imshow("Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()