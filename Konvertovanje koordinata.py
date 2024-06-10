import pyproj
import numpy as np
from pyproj import Transformer

lat, lon = 44.799250, 20.407844
lat_ca,lon_ca = 44.799250, 20.407844
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Toplana Novi Beograd")

lat, lon = 44.828996, 20.420443 
lat_ca,lon_ca = 44.828996, 20.420443 
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Hotel Jugoslavija")

lat, lon = 44.761005668795505, 20.468322252322753
lat_ca,lon_ca = 44.761005668795505, 20.468322252322753
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Policijska akademija")

lat, lon = 44.822760093262694, 20.384602933522473 
lat_ca,lon_ca = 44.822760093262694, 20.384602933522473
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Trafostanica Bezanijska kosa")

lat, lon = 44.82521551005593, 20.418565566224927
lat_ca,lon_ca = 44.82521551005593, 20.418565566224927
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Ambasada Kine")

lat, lon = 44.81596306620656, 20.43822653187824
lat_ca,lon_ca = 44.81596306620656, 20.43822653187824
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Poslovni centar Usce")

lat, lon = 44.81082135384928, 20.470185465884732 
lat_ca,lon_ca =44.81082135384928, 20.470185465884732  
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Zgrada RTS")

lat, lon = 44.742776136634824, 20.318683836581368
lat_ca,lon_ca = 44.742776136634824, 20.318683836581368
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Most na Savi Ostruznica")

lat, lon = 44.69668508444535, 20.514743371136763
lat_ca,lon_ca = 44.69668508444535, 20.514743371136763
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "Avalski toranj")

lat, lon = 44.480891266294556, 20.293570473810256 
lat_ca,lon_ca = 44.480891266294556, 20.293570473810256 
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "TE Kolubara Veliki Crljeni")

lat, lon = 44.77787334582087, 20.45737089730074
lat_ca,lon_ca = 44.77787334582087, 20.45737089730074
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "KBC Dragisa Misovic")

lat, lon = 44.672064290658234, 20.16172070366416
lat_ca,lon_ca = 44.672064290658234, 20.16172070366416
trans_GPS_to_XY = Transformer.from_crs(4326, 6316)
gps = (lat_ca,lon_ca) # centar  Ca
xy = trans_GPS_to_XY.transform(gps[0], gps[1])
print(xy, "TE Nikola Tesla")
