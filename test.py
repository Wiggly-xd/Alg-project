from descartes import PolygonPatch
from PIL import Image
from matplotlib import pyplot as plt
import shapefile
import matplotlib
import os
#from scipy import imageio
import numpy
file=shapefile.Reader("Export_Output_387.shp");
#file=shapefile.Reader("countries.shp")
rec=file.record(2)
fig=plt.figure(figsize=(10, 10))
ax=fig.gca()
shapes=file.shapes()
print(len(shapes))

for i in range(len(shapes)):
    try:
        poly=file.shape(i).__geo_interface__
        ax.add_patch(PolygonPatch(poly, fc='#ffffff', ec='#000000', alpha=0.5, zorder=2 ))
        ax.axis('scaled')
        ax.append(fig.add_subplot(5, 4))
        fig(num=1, figsize=(8, 6))
        ax.patch.set_alpha(0.5)

    except:
        print (i)
img=Image.open(r"1406_S1_2020.bmp")
        #plt.imshow(img)

#img=Image.open("img.png")
print("true");
pixVal=list(img.getdata())
for i in pixVal:
    if(i!=(0, 255, 0) and i!=(204, 232, 182) and i!=(252, 251, 210) and i!=(242, 213, 199)and i!=(224, 160, 128) and i!=(197, 224, 245)):
        array=numpy.where(img==i)
        coordinates=zip(array[0])
        unique=list(set(list(coordinates)))
        for j in array:
            print(j);
    if i==(90, 90, 160):
        break
#img=img.resize((6000, 8000))
#plt.subplot(1, 2, 1)
plt.imshow(img, alpha=0.5)

plt.show()
