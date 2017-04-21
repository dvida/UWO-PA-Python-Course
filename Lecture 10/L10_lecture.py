from __future__ import print_function

import matplotlib.pyplot as plt

from astroquery.sdss import SDSS
from astropy import units


# Photoobj_fields: UGRIZ
# UGRIZ: http://www1.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/community/CFHTLS-SG/docs/extra/sdsscfhtlsugriz.gif

# Let's get g and r magnitudes of stars in the globular cluster M13, in the 10 arcmin radius
result_table = SDSS.query_region('m13', radius=10*units.deg/60, photoobj_fields=['ra', 'dec', 'g', 'r'])

# Stars in the random part of the sky, with no clusters (stars at r = 22 and g-r = 0.5 are halo stars)
#result_table = SDSS.query_region('22h46m24.00s +31d42m00.0s', radius=0.5*units.deg, photoobj_fields=['ra', 'dec', 'g', 'r'])

# Start in the random part of the sky (with a cluster in the halo!) - Monoceros Ring
# result_table = SDSS.query_region('7h40m48.00s +32d42m00.0s', radius=0.5*units.deg, photoobj_fields=['ra', 'dec', 'g', 'r'])


print(result_table)

r_mags = []
gr_mags = []

for row in result_table:

    g = row[2]
    r = row[3]

    # Skip empty values (-9999.0)
    if (g < 0) or (r < 0):
        continue

    r_mags.append(r)
    gr_mags.append(g - r)


plt.scatter(gr_mags, r_mags, s=0.05, c='black')

plt.xlabel('g-r')
plt.ylabel('r')

plt.xlim([-1, 2.5])
plt.ylim([22, 15])

plt.show()

# Blue stars are at the left, red stars are at the right.
# Why? Let's say that the g magnitude of a star is 10. If the star is brighter in red, let's say r_mag = 8,
# then the g-r will be 2, thus to the right of the graph.

# Does this remind you of some other graph that you may have seen? Some graph that has blue start on the left
# and red stars on the right?
# Of course, the Hertzsprung-Russell diagram!

# This is a classic HR diagram of a globular cluster, a group of star that are of the same age and distance.


# Lecture note: Now show how the CMD looks like for a random part of the sky.

# Lecture note: Then show how the CMD looks like for the Monoceros Ring stars.
#   This is now it was found that the Milky Way is in the process of merging with another galaxy.



#######################

### Dependencies ###

# Dependencies are external libraries which are used by our code.
# During this lecture, we were using numpy, scipy, matplotlib, scikit-learn, etc.; all Python libraries 
# written by other people.

# OK, where's the problem here?
# - Libraires are updated, they change, functions that you using the v1.0 of the library do not exist at
#   all in the v2.0 of the library. 
# - Some libraries introduce additional dependencies, and those dependences may have their own dependences,
#   which in turn may have their own dependences...
# - Some libraries are dependant on specific versions of some other library. E.g. let's say you have a 
#   library A which is dependant on v1.2 of B. And then you have library C which is dependant on v2.5 of 
#   library B...
# - It is possible to have circular dependencies - some libraries are dependant on one another, which cannot
#   be solved easily.

# The whole thing is called "Dependency Hell".

# Let me show you one dependency horror story:
# http://www.haneycodes.net/npm-left-pad-have-we-forgotten-how-to-program/


# Takeaway: Be careful when using a lot of libraries in your code, and avoid downloading whole libraries just
# for one function.

# Recommendation for Python: Try to stick to libraries which are in the Anaconda package, as people make sure
# they will play nice with each other.


#######################

### Cython ###

# Now we will take a look how to use cython to speed up our Python code by converting it to C!

