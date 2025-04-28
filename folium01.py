# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 07:53:43 2025

@author: asgun
"""

import folium
import pandas as pd

# Create a map object centered at latitude 40.73 and longitude -73.99 (New York City)
m = folium.Map(location=[-34, -49], zoom_start=10)


# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
   'lat':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
   'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
   'value':[10, 12, 40, 70, 23, 43, 100, 43]
})

import math
# add marker one by one on the map, and account for Mercator deformation
for city in data.itertuples():
    local_deformation = math.cos(city.lat * math.pi / 180)
    folium.Circle(
        location=[city.lat, city.lon],
        popup='%s (%.1f)' % (city.name, city.value),
        radius=city.value * 20000.0 * local_deformation,
        color='crimson',
        fill=True,
        fill_color='crimson'
    ).add_to(m)



# Save the map to an HTML file
m.save("my_map.html")
    