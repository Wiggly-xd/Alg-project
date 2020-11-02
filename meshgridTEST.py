from descartes import PolygonPatch
from PIL import Image
import shapefile
import matplotlib
import matplotlib.patches as patches
import os
import numpy as np
import matplotlib.pyplot as plt

x_min = 1 
x_max = 16
y_min = 1 
y_max = 12
Nx = 16 #number of steps for x axis
Ny = 12 #number of steps for y axis

x = np.linspace(x_min, x_max, Nx)
y = np.linspace(y_min, y_max, Ny)

#Can then create a meshgrid using this to get the x and y axis system
xx, yy = np.meshgrid(x, y)
#If you already have some function that returns an RGB tuple
def somefunc(x_value, y_value):
    if x_value > 2 and y_value < 3:
        return np.array(((y_value+1)/4., (y_value+2)/5., 0.43))
    elif x_value <=2:
        return np.array((y_value/5., (x_value+3)/5., 0.0))
    else:
        return np.array((x_value/5., (y_value+5)/10., 0.89))

img=Image.open(r"img_shp/1406_S1_2020.bmp")
pixVal=list(img.getdata())
width, height=0,0
cordinates=width,height
Mwidth, Mheight = img.size
colors=[]


# you may loop over the grid to fill a new array with those values
res = np.zeros((xx.shape[0],xx.shape[1],3))
for i in range(xx.shape[0]):
    for j in range(xx.shape[1]):
        res[i,j,:] = somefunc(xx[i,j],yy[i,j])



plt.figure(dpi=100)
plt.imshow(res)