# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:58:54 2019

@author: Ana Karina Bentes
"""

'''
========================================
Gráficos 3D com Perfis de Contorno
========================================

'''

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import cm
import numpy as np


from deap import benchmarks

def rastrigin_arg0(sol):
    return benchmarks.rastrigin(sol)[0]

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = np.fromiter(map(rastrigin_arg0, zip(X.flat,Y.flat)), dtype=np.float, count=X.shape[0]*X.shape[1]).reshape(X.shape)
# Plot the 3D surface
#ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0.2)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
ax.contour(X, Y, Z, zdir='z', offset= 0, cmap=cm.jet)
#cset = ax.contour(X, Y, Z, zdir='x', offset=-30, cmap=cm.coolwarm)
#cset = ax.contour(X, Y, Z, zdir='y', offset=30, cmap=cm.coolwarm)

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
#ax.set_zlim(0, 5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))

cbar = fig.colorbar(surf, ticks=(np.arange(0,80,4)))
#cbar.ax.set_yticklabels(np.arange(0,80,4))
fig.tight_layout()
plt.savefig('rastrigin.png', dpi=150)
