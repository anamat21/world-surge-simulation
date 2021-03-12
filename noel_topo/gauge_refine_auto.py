
from __future__ import absolute_import
from __future__ import print_function

import os

import numpy as np
import matplotlib.pyplot as plt
import datetime

import clawpack.visclaw.colormaps as colormap
import clawpack.visclaw.gaugetools as gaugetools
import clawpack.clawutil.data as clawutil
import clawpack.amrclaw.data as amrclaw
import clawpack.geoclaw.data as geodata


import clawpack.geoclaw.surge.plot as surgeplot

OUT = os.path.join(os.environ.get('OUT_DIR', '_output'))

## follow storm

track = surgeplot.track_data(os.path.join(OUT, 'fort.track'))

print(track)

from __future__ import absolute_import
from __future__ import print_function

import os

import numpy as np
import matplotlib.pyplot as plt
import math
import random
import datetime

import clawpack.visclaw.colormaps as colormap
import clawpack.visclaw.gaugetools as gaugetools
import clawpack.clawutil.data as clawutil
import clawpack.amrclaw.data as amrclaw
import clawpack.geoclaw.data as geodata

from clawpack.geoclaw import topotools
import clawpack.geoclaw.surge.plot as surgeplot

OUT = os.path.join(os.environ.get('OUT_DIR', '_output'))
DATA = os.path.join(os.environ.get('DATA_DIR', os.getcwd()))

## topo
topo_path = os.path.join(DATA, 'topo_for_noel.tt3')
topo = topotools.Topography()
topo.read(topo_path, topo_type=3)

## follow storm

track = surgeplot.track_data(os.path.join(OUT, 'fort.track'))

shoreline = topo.make_shoreline_xy()

plt.figure(figsize = [12,10])
topo.make_shoreline_xy()

for n in np.arange(0,32,2):
    track_data = track.get_track(n)
    print(track_data)
    plt.scatter(track_data[0], track_data[1])
    
    
track_data = track.get_track(1)
print(near_shoreline(track_data[0], track_data[1], shoreline))     
    
## returns shoreline closest to storm
def near_shoreline(storm_x, storm_y, shoreline):
    
    point_x = random.uniform(storm_x - 10, storm_x + 10)
    point_y = random.uniform(storm_y - 10, storm_y + 10)
    
    dis = []
    
    for n in shoreline:
        dis.append((distance(storm_x, storm_y, n[0], n[1])))
        
    print(min(dis))
    minimum = dis.index(min(dis))
    print(shoreline[minimum])
    return minimum
    
## find distance between two points    
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    return distance
