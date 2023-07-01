import numpy as np
from mpl_toolkits.basemap import Basemap
from itertools import chain
import matplotlib.pyplot as plt
from PIL import Image

def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)

    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)

    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')

def createworld_map(x,y):

    fig = plt.figure(figsize=(8, 6), edgecolor='w')
    m = Basemap(projection='cyl', resolution=None,
                llcrnrlat=-90, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180, )

    m.scatter(y, x, latlon=True, s=150, marker="x", color="r")
    draw_map(m)
    fig.savefig('dashboard\static\images\worldMap.png')

    im = Image.open(r"dashboard\static\images\worldMap.png")
    width, height = im.size
    left = 90
    top = 130
    right = 730
    bottom = 470
    im1 = im.crop((left, top, right, bottom))
    im1.save("dashboard\static\images\worldMap.png")
    plt.close('all')


def createUS_map(x,y):

    fig = plt.figure(figsize=(8, 6), edgecolor='w')
    m = Basemap(projection='cyl', resolution=None,
                llcrnrlat=24, urcrnrlat=50,
                llcrnrlon=-125, urcrnrlon=-61,)

    m.scatter(y, x, latlon=True, s=150, marker="X", color="r")
    draw_map(m)
    fig.savefig(r"dashboard\static\images\USMap.png")

    im = Image.open(r"dashboard\static\images\USMap.png")
    width, height = im.size
    left = 90
    top = 130
    right = 730
    bottom = 470
    im1 = im.crop((left, top, right, bottom))
    im1.save(r"dashboard\static\images\USMap.png")
    plt.close('all')

def coordSort(coords):
    x = []
    y = []
    for i in range(1,21):
         c = getattr(coords, 'coord_' + str(i))
         if (c != 0.0):
             if (i % 2):
                 x.append(c)
             else:
                 y.append(c)

    createworld_map(x,y)
    createUS_map(x,y)
