from descartes import PolygonPatch
from PIL import Image
import matplotlib
import matplotlib.patches as patches
import os
import numpy as np
import matplotlib.pyplot as plt

# Make some random data to represent your r, g, b bands.
ny, nx = 2, 3
img=Image.open(r"img_shp/1406_S1_2020.bmp")
pixVal=list(img.getdata())
width, height=0,0
cordinates=width,height
Mwidth, Mheight = img.size
rgb_im = img.convert('RGB')
for i in pixVal:
    if i==(90, 90, 160):
        break
    cordinate = x, y = width, height
    r,g,b=img.getpixel(cordinate)
    #if(color!=(0,255,0)):
    #    print(color)
    r, g, b = [np.random.random(ny*nx).reshape((ny, nx)) for _ in range(3)]
print(r)
print("")
print(g)
print("")
print(b)


c = np.dstack([r,g,b])

plt.imshow(c, interpolation='nearest')
plt.show()