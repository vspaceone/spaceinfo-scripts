#run this script on startup ONCE
#some of the functions are copied from https://wiki.cccgoe.de/wiki/Pixelflut. thanks guys

import socket, time, os, sys
from PIL import Image

time.sleep(30)
os.chdir(sys.path[0])

pxf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pxf.connect(('localhost',1337))

def send_pixel(x,y,r,g,b):
    cmd = 'PX %d %d %02x%02x%02x\n' % (x,y,r,g,b)
    pxf.send(cmd.encode())

#send info image
img = Image.open('pxf_useage.bmp').convert('RGB')
_,_,w,h = img.getbbox()  
for x in range(0, w-1):
   for y in range(0, h-1):
     r,g,b = img.getpixel((x,y))
     send_pixel(x,y,r,g,b)
