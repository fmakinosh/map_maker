# --- * --- * --- * ---
# [ Map maker ]

# Copyright (c) [2019] [fmakinosh]

# This software is released under the MIT License.
# https://github.com/fmakinosh/map_maker
# --- * --- * --- * ---
#
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

# === params ===

min_lon = 130.0
max_lon = 155

min_lat = 30
max_lat = 50

# ==============

fig = plt.figure(figsize=(7,7))
m = Basemap(projection='merc',
            resolution='h',
            llcrnrlon = min_lon,
            llcrnrlat = min_lat,
            urcrnrlon = max_lon,
            urcrnrlat = max_lat)

m.drawcoastlines(color='black', linewidth=0.5)
m.drawcountries(color='black', linewidth=0.5)
m.fillcontinents(color='whitesmoke',lake_color='powderblue');
m.drawmapboundary(fill_color='powderblue')

m.drawmeridians(np.arange(0, 360, 10), labels=[1,0,0,1], labelstyle='+/-')
m.drawparallels(np.arange(-90, 90, 10), labels=[1,0,0,1], labelstyle='+/-')

x_eq = [
-73.407,
139.197,
141.568,
143.91,
95.982,
153.266,
154.524,
-172.095,
-72.898,
142.373,
93.063,
174.337,
174.152,
131.825,
-70.769,
173.054,
141.387
]

y_eq = [
-38.143,
42.851,
38.849,
41.815,
3.295,
46.592,
46.243,
-15.489,
-36.122,
38.297,
2.327,
-41.704,
-41.734,
33.684,
-19.61,
-42.737,
37.393
]

x,y = m(x_eq, y_eq)

m.scatter(x, y, c='darkorchid', edgecolor='k', linewidth=0.3, s=77, zorder=100)

# --- fig at upper left
ax2 = fig.add_subplot(3,3,1)

m2 = Basemap(projection='ortho',
             resolution='i',
             lon_0 = (min_lon + max_lon) / 2,
             lat_0 = (min_lat + max_lat) / 2)

m2.drawcoastlines(color='black', linewidth=0.5)
m2.drawcountries(color='black', linewidth=0.5)
m2.fillcontinents(color='whitesmoke',lake_color='powderblue');
m2.drawmapboundary(fill_color='powderblue')

lons = [min_lon, max_lon, max_lon, min_lon]
lats = [min_lat, min_lat, max_lat, max_lat]

x_r, y_r = m2(lons, lats)
xyr = list(zip(x_r, y_r))

poly = Polygon(xyr, facecolor='none', edgecolor='r')

ax2.add_patch(poly)

plt.savefig('map.png',dpi=300)
