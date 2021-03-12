from __future__ import absolute_import
from __future__ import print_function
import os
import datetime
import shutil
import gzip

import numpy as np

from clawpack.geoclaw.surge.storm import Storm
import clawpack.clawutil as clawutil
from clawpack.geoclaw import topotools

CLAW = os.environ['CLAW']

datadir = os.path.join(CLAW,'geoclaw','noel') # directory with noel topo data

# use topography data from seperate noel directory
topo_path_nc = os.path.join(datadir, 'noel_topo.nc')
noel_topo = topotools.read_netcdf(topo_path_nc, coarsen=2, verbose=True)

# make netcdf file into .tt3 topography file
noel_topo.write(os.path.join(datadir, 'topo_for_noel.tt3'), topo_type=3, header_style='geoclaw', Z_format='%15.7e')
