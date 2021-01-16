#! /usr/bin/python3
## Inspired by https://www.hackerearth.com/practice/notes/extracting-pixel-values-of-an-image-in-python/
from PIL import Image
im = Image.open('twins.png', 'r')
print(im.format, im.size, im.mode)
pix_val = list(im.getdata())  #dump the mess
pix_val_flat = [x for sets in pix_val for x in sets]
## examine the values a bit
print("Analyzing RGB values")
#print("Checking if any A values other than 255")  #NOPE!
#for val in pix_val:
#    if val[3] != 255:
#        print(val)
#        
rgb_val = [x[0:3] for x in pix_val]
print(rgb_val[0])

with open('twins-rgb.txt', 'w') as f:
   for val in rgb_val:
       f.write(str(val))
