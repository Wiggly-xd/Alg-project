from descartes import PolygonPatch
from PIL import Image
from matplotlib import pyplot as plt
import shapefile
import matplotlib
import matplotlib.patches as patches
import matplotlib.colors as color
import os
#from scipy import imageio
import numpy
def rgb_to_hex(rgb):
    return '#'+'%02x%02x%02x' % rgb

file=shapefile.Reader("img_shp/Export_Output_387.shp")
#file=shapefile.Reader("img_shp/AFO6.shp");
#rec=file.record(2)
fig=plt.figure(figsize=(10, 10))
ax=fig.gca()
shapes=file.shapes()
howManyShapes=len(shapes)
s=file.shape()
shape=shapes[0].points
contain=file.bbox
print("ShapePoints",shape)
print("Kordinater",contain)

längd=contain[2]-contain[0]
höjd=contain[3]-contain[1]
print("Längd= ",längd)
print("Höjd= ",höjd)
print("Propottioner mellan bmp fil och shapefil längd= ",längd/1600)
print("Propottioner mellan bmp fil och shapefil höjd= ",höjd/1200)
widthDif=längd/1600
heightDif=höjd/1200
print(file)
#Kordinat av shape 0
print("Shape coord",len(shapes[0].bbox))
for i in range(howManyShapes):
    try:
        poly=file.shape(i).__geo_interface__
        ax.add_patch(PolygonPatch(poly, fc='#ffffff', ec='#000000', alpha=0.5, zorder=2 ))
        ax.axis('scaled')
        ax.append(fig.add_subplot(5, 4))
        fig(num=1, figsize=(8, 6))
        ax.patch.set_alpha(0.5)
    except:
        print (i)
img=Image.open(r"img_shp/1406_S1_2020.bmp")
        #plt.imshow(img)

print("true")
pixVal=list(img.getdata())
#x, y = (img > 1000).nonzero()
#vals=img[x, y];
width, height=0,0
cordinates=width,height
Mwidth, Mheight = img.size
outside=0
Skogsmark=0
Vatten=0
Myrmark=0
houses=0
avverkad=0
for i in pixVal:
    if i==(90, 90, 160):
        break
    cordinate = x, y = width, height
    if(i==(0, 255, 0)):
        outside=outside+1
    elif(i==(204, 232, 182)):
        Skogsmark=Skogsmark+1
    elif(i==(197, 224, 245)):
        Vatten=Vatten+1
    elif(i==(242, 213, 199)):
        Myrmark=Myrmark+1
    elif(i==(224, 160, 128)):
        houses=houses+1
        colors=rgb_to_hex(i)
        print(width)
        print(height)
        rect = patches.Rectangle((387729+(width*widthDif),6464316+(height*heightDif)),widthDif,heightDif,linewidth=1,facecolor=colors)
        ax.add_patch(rect)
    else:
        avverkad=avverkad+1
    width=width+1
    if width==1200:
        width=0
        height=height+1

size=Mwidth*Mheight
print("outside ",outside)
print("Skogsmark ",Skogsmark)
print("Vatten ",Vatten)
print("Myrmark ",Myrmark)
print("hus ",houses)
print("avverkad ",avverkad)
print("total size ",size)
print("Inte med ",size-outside-Skogsmark-Vatten-Myrmark-houses-avverkad)

plt.show()
