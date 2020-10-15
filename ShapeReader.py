import geopandas as gpd

gdf1 = gpd.read_file('shapefiles/Export_Output_387.shp')
gdf2 = gpd.read_file('shapefiles/AFO6.shp')

gdf = gpd.GeoDataFrame(pd.concat([gdf2,gdf1]))

gdf.head()
gdf.plot(cmap='OrRd', scheme='quantiles')


#https://stackoverflow.com/questions/56905631/combining-shapefiles-in-python-geopandas