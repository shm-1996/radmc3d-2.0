import problem_setup as p
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt
from matplotlib import cm
from radmc3dPy.image import *    # Make sure that the shell variable PYTHONPATH points to the RADMC-3D python directory
from radmc3dPy.analyze import *  # Make sure that the shell variable PYTHONPATH points to the RADMC-3D python directory
from radmc3dPy.natconst import * # Make sure that the shell variable PYTHONPATH points to the RADMC-3D python directory

#
# Make sure to have done the following beforhand:
#
#  First compile RADMC-3D
#  Then run:
#   python problem_setup.py
#   radmc3d mctherm
#

#
# View a 2-D slice of the 3-D array of the setup
#
rr   = p.rr[:,:,0]
tt   = p.tt[:,:,0]
zzr  = np.pi/2-tt
rhod = p.rhod[:,:,0]
fig1 = plt.figure()
ax   = fig1.gca(projection='3d')
ax.plot_surface(np.log10(rr)/au, zzr, np.log10(rhod), rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=1, antialiased=False)
#ax.set_zlim3d(0, 10)

#
# Make and plot an example image
#
fig2  = plt.figure()
makeImage(npix=200,incl=60.,phi=30.,wav=30.,sizeau=300)   # This calls radmc3d 
a=readImage()
plotImage(a,log=True,au=True,maxlog=6,cmap='hot')

#
# Make and plot the SED as seen at 1 pc distance
#
#os.system("radmc3d sed incl 60 phi 30")
#fig3  = plt.figure()
#s     = readSpectrum()
#lam   = s[:,0]
#nu    = 1e4*cc/lam
#fnu   = s[:,1]
#nufnu = nu*fnu
#plt.plot(lam,nufnu)
#plt.xscale('log')
#plt.yscale('log')
#plt.axis([1e-1, 1e4, 1e-10, 1e-4])
#plt.xlabel('$\lambda\; [\mu \mathrm{m}$]')
#plt.ylabel('$\\nu F_\\nu \; [\mathrm{erg}\,\mathrm{cm}^{-2}\,\mathrm{s}^{-1}]$')
