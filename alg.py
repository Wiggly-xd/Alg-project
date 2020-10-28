import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib
from PIL import Image
import time

gdf1 = gpd.read_file('img_shp/Export_Output_387.shp')

#gdf2 = gpd.read_file('img_shp/AFO6.shp')

gdf = gpd.GeoDataFrame(pd.concat([gdf1]))
#example of how to print the boundry coordinates for a polygon.
frame=gdf.bounds
limit=gdf.total_bounds
print (limit)
# create a point object containing the coordinates of the poit you want to check. this is needed later. then in this example we call the function then take a polygon via the index from our gdf data frame. and then extract the shape from that index.  
offsety=6464316.734
offsetx=387729.442
x1 = 1600/2
y1 = 1300
scala = 58.7
x1*=scala
y1*=scala
p1=Point(x1+offsetx,y1+offsety)
print(x1)
#p1=Point(419633, 6484949)
def isWithin(point, frame):
    for i in range(62):
        if point.within(frame.iloc[i].geometry):
            return i
#gdf.geometry = gdf.geometry.scale(xfact=1/10000, yfact=1/10000, zfact=1.0, origin=(0, 0))

gdf.head()
gdf.plot(cmap='OrRd', scheme='quantiles')
def getCoordinate(offsetx,offsety):
    coordinate=[]

    #img=Image.open(r"img_shp/test.bmp")
 #   t0 = time.time()
    img=Image.open(r"img_shp/1406_S1_2021.bmp")
    pixVal=list(img.getdata())
    width, height=0,0
    for i in pixVal:
        cordinate = width, height
        width=width+1
        if width==1346:
            width=0
            height=height+1
        if i!=(0, 255, 0) and i!=(197, 224, 245):
            coordinate.append([Point(width*57.8+offsetx,height*57.8+offsety),i])
#    t1 = time.time()
#    total = t1-t0
#    print(total/60)
  #  arrays.append(coordinate)
  #  arrays.append(color)
    return coordinate
CoordinateColor=getCoordinate(offsetx,offsety)
for x in CoordinateColor:
    i=isWithin(x[0], gdf)
#    if i !=None:
    print(i);
        #print(isWithin(x, gdf))