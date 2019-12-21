import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import os
import descartes

# import folium
# plt.rcParams['figure.figsize'] = (10,8)

data_pth = "./Data/"
usa= gpd.read_file(os.path.join(data_pth, 'states.shp'))

cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
cities = gpd.read_file(os.path.join(data_pth, "ne_10m_populated_places.shp"))
uscities = cities.query('ADM0NAME == "United States of America"')

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

def state_plotter(states, us_map=True):
    fig, ax = plt.subplots(figsize=(10,8))
    #turns the axis off
    ax.axis('off')

    #adds a title
    ax.set_title("MeMD Diagnosis Across the US", fontdict={'fontsize': '25', 'fontweight' : '3'})

    if us_map:
        if 'HI' in states:
            usa[0:50].plot(ax=ax, alpha = 0.3)
        elif 'AK' in states:
            usa[1:51].plot(ax=ax, alpha = 0.3)
        elif 'AK' and 'HI' in states:
            usa[0:51].plot(ax=ax, alpha = 0.3)
        else:
            usa[1:50].plot(ax=ax, alpha = 0.3)
        #ax=ax makes the map plot on the initial matplotlib figure
        for n in states:
            usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth = 1)

    elif us_map == False:
        for n in states:
            usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth =2)

# m = folium.Map(location=[45.5236, -122.6750])

# usa[usa.STATE_ABBR == 'TX'].plot()
# usa[usa.SUB_REGION == 'East North Central'].plot()
# base = usa.plot(state_plotter(['LA', 'AR']))
# base = state_plotter(['LA', 'AR'])

base = usa.plot(state_plotter(['LA', 'AR', 'MO', 'CO', 'UT', 'NM', 'TX', 'CA', 'NV', 'MS', 'IL', 'KY', 'TN', 'WV', 'SC','NC', 'OK', 'MD', 'KS', 'IL', 'ID', 'WY', 'NE', 'DC', 'VA', 'PA', 'MN', 'IA', 'AZ']))
uscities.plot(ax=base,figsize=(15,10), color='orange', markersize= 1)

fig, x = plt.subplots(1, 1)
world.plot(column='pop_est', ax=x, legend=True, figsize=(15,10))


# usa.plot()
plt.show()
