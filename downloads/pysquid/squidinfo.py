#!/usr/bin/python -tt

# -------------------------- LICENSE -----------------------------------
#
# This file is part of the LibSQUID software libraray.
#
# LibSQUID is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LibSQUID is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with LibSQUID.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2014 James Wren and Los Alamos National Laboratory
#

import os
import sys
import pysquid as ps

# get args
if (len(sys.argv) < 3):
    print "Get information on a particular squid index."
    print "calling sequence: squidinfo.py projection squid"
    print "projections: 0=TSC, 1=CSC, 2=QSC, 3=HSC"
    print "output angles in degrees"
    sys.exit()
projection=int(sys.argv[1])
if (projection == 0):
   print "TSC Projection."
elif (projection == 1):
   print "CSC Projection."
elif (projection == 2):
   print "QSC Projection."
elif (projection == 3):
   print "HSC Projection."
else:
   print "Undefined projection, using HSC."
   projection=3
squid=long(sys.argv[2])

# Make sure squid is valid
if (ps.squid_validate(squid) == 0):
   print "Invalid squid argument!"
   sys.exit()

# Get basic squid information
[retval,x,y,face,k]=ps.squid2xyfk(squid)
if (retval == -1):
   print "squid2xyfk failed!"
   sys.exit()

# Get squid center
[retval,lon,lat]=ps.squid2sph(projection,squid)
if (retval == -1):
   print "squid2sph failed!"
   sys.exit()

# Get squid corners
[retval,clon,clat]=ps.squid_corners(projection,squid)
if (retval == -1):
   print "squid_corners failed!"
   sys.exit()

# Print out information
print "SQUID={:d}".format(squid)
print "LEVEL={:d}, FACE={:d}, X={:d}, Y={:d}".format(k,face,x,y)
print "CENTER LON={:.6f} LAT={:.6f}".format(lon/ps.DD2R, lat/ps.DD2R)
for i in range(4):
   print "CORNER {:d}: LON={:.6f} LAT={:.6f}"\
       .format(i,clon[i]/ps.DD2R,clat[i]/ps.DD2R)
