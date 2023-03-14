#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:00:10 2023

@author: hi00vyta
"""
'''
You can obtain a concatenated image in which multiple images are arranged in 
a row vertically and horizontally using the Pillow packege and the function defined bellow.

https://note.nkmk.me/en/python-pillow-concat-images/
https://www.tutorialspoint.com/python_pillow/python_pillow_cropping_an_image.htm

'''
#Import required Image library
from PIL import Image
#from PIL import ImageFont
#from PIL import ImageDraw

## open your desired picture
im1 = Image.open('pic1.png')
## open thompson tetrahedron
imTT = Image.open('TT.png')
print('im1=',im1.size)
print('imTT=',imTT.size)

### crop pictures
im1= im1.crop((0,0,800,500))
imTT=imTT.crop((120,0,1024,700))
# imTT.show()
# im1.show()

### resize pictures
imTT= imTT.resize((round(imTT.size[0]*0.2), round(imTT.size[1]*0.2)))

# imSS.show()
# print(imTT.size)

# creat a big back ground image, for transparent background use color=(255,255,255,0)
def get_concat(im1,imTT):
    dst = Image.new('RGBA', (im1.width, im1.height), color="white")
    
    dst.paste(im1, (0,0))
    dst.paste(imTT, (340, 40))
    
    return dst

all_stresses=get_concat(im1,imTT)
all_stresses.show()
all_stresses.save('final.png')



