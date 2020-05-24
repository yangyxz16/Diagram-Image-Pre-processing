# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Improting Image class from PIL module 
from PIL import Image 

im = Image.open(r"C:\Users\yangy\Desktop\0001.jpg") 
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 

# Setting the points for cropped image 
left = 0
top = height / 2
right = width / 2
bottom = height * 0.88

# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

im2 = im1.convert('L')


im2.show();