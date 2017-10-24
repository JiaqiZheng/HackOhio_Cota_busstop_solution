# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import Voronoi, voronoi_plot_2d

df=pd.read_csv("cota.csv")
stop_lat=df['stop_lat']
stop_lon=df['stop_lon']

x_y = {'x' : stop_lon, 'y': stop_lat}
bus_stop_loc=pd.DataFrame(x_y)
vor = Voronoi(bus_stop_loc)

data=pd.read_csv("cubic.csv")
end=np.ndarray(shape=(2,data.shape[0]))

for i in range(data.shape[0]):
    track=data.iloc[[i]].values
    track=track[0]
    track=track[0]
    track = track.split('],[')
    end_0=track[len(track)-1][:-2]
    end[0][i]=float(end_0.split(',')[0])
    end[1][i]=float(end_0.split(',')[1])

data=pd.read_csv("cubic.csv")
start=np.ndarray(shape=(2,data.shape[0]))

for i in range(data.shape[0]):
    track=data.iloc[[i]].values
    track=track[0]
    track=track[0]
    track = track.split('],[')
    start_0=track[0][2:]
    start[0][i]=float(start_0.split(',')[0])
    start[1][i]=float(start_0.split(',')[1])

voronoi_plot_2d(vor,show_points=False,show_vertices=False)
plt.scatter(end[0],end[1], color='b')

plt.show()











