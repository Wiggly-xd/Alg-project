import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib
gdf1 = gpd.read_file('img_shp/Export_Output_387.shp')

#gdf2 = gpd.read_file('img_shp/AFO6.shp')

gdf = gpd.GeoDataFrame(pd.concat([gdf1]))
frame=gdf.bounds
print(frame.iloc[1])
# create a point object containing the coordinates of the poit you want to check. this is needed later. then in this example we call the function then take a polygon via the index from our gdf data frame. and then extract the shape from that index.  
p1=Point(419633, 6484949)
def isWithin(point, frame):
    for i in range(62):
        if point.within(frame.iloc[i].geometry):
            print ("true")
            print(i)
isWithin(p1, gdf)
#print(frame.iloc[1, 1])

gdf.head()
gdf.plot(cmap='OrRd', scheme='quantiles')