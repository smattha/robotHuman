# https://api.open-elevation.com/api/v1/lookup

from global_land_mask import globe
import numpy as np
# //https://github.com/toddkarin/global-land-mask
# Check if a point is on land:
lat = 38.212023
lon =21.700340
is_on_land = globe.is_land(lat, lon)

print('lat={}, lon={} is on land: {}'.format(lat,lon,is_on_land))
# lat=40, lon=-120 is on land: True

# # Check if several points are in the ocean
# lat = 40
# lon = np.linspace(-150,-110,3)
# is_in_ocean = globe.is_ocean(lat, lon)
# print('lat={}, lon={} is in ocean: {}'.format(lat,lon,is_in_ocean))
# # lat=40, lon=[-150. -130. -110.] is in ocean: [ True  True False]
