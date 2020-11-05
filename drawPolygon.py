import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib
from PIL import Image, ImageDraw, ImageFont
import time
import numpy as np

img=Image.open(r"img_shp/1406_S1_2021.bmp")

gdf1 = gpd.read_file('img_shp/Export_Output_387.shp')
counter=0
for index,test in gdf1.iterrows():
    if index==29:
        #poly=test.geometry
        for poly in test.geometry:
            array = np.array(poly.exterior)
            for coordinate in array:
                x=coordinate[0]
                y=coordinate[1]
                offsety=6464316.734
                offsetx=387729.442
                scala = 69
                x-=offsetx
                y-=offsety
                x=int(x/scala)
                y=int(y/scala)
                y=y*-1
                x=x-30
                y=y+24
                #print(x)
                #print(y)
                img.putpixel((x,y), (0, 0, 0))
        
    #array.append(test.geometry)
    #img.putpixel((test.geometry), (0, 0, 0))
    counter=1
#im = ImageDraw.Draw(img)
#im = im.point((1, 1), fill="white")
#img.putpixel((1, 1), (0, 0, 0))
#img.save()
img.show()
#ImageDraw.point(1,1, fill="Black")
