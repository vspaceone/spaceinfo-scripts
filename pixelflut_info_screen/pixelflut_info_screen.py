#run this script on startup ONCE
#some of the functions are copied from https://wiki.cccgoe.de/wiki/Pixelflut. thanks guys

import socket
from PIL import Image

pxf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pxf.connect(('localhost',1337))

def send_pixel(x,y,r,g,b):
    pxf.send('PX %d %d %02x%02x%02x\n' % (x,y,r,g,b))

#send info image
img = Image.open('pxf_useage.bmp').convert('RGB')
_,_,w,h = img.getbbox()  
for x in range(w-1, 0):
   for y in range(h-1, 0):
     r,g,b = img.getpixel((x,y))
     send_pixel(x,y,r,g,b)
