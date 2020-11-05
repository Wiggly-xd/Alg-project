import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
gdf = gpd.read_file('img_shp/Export_Output_387.shp')

#gdf2 = gpd.read_file('img_shp/AFO6.shp')

#gdf = gpd.GeoDataFrame(pd.concat([gdf1]))
frame=gdf.bounds
print(frame.iloc[2, 2])
print(gdf)
gdf['geometry'].plot()
plt.show()