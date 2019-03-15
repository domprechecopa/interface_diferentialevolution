# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:40:10 2019

@author: Ana Karina Bentes
"""

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

def rosenbrock_arg0(sol):
    return benchmarks.rosenbrock(sol)[0]

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-1.5, 1.5, 0.05)
Y = np.arange(-1.5, 2, 0.05)
X, Y = np.meshgrid(X, Y)
Z = np.fromiter(map(rosenbrock_arg0, zip(X.flat,Y.flat)), dtype=np.float, count=X.shape[0]*X.shape[1]).reshape(X.shape)
# Plot the 3D surface
#ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
ax.view_init(elev=44, azim=-65)
surf = ax.plot_surface(X, Y, Z, norm=LogNorm(), rstride=1, cstride=1, cmap=cm.jet, linewidth=0.2)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
ax.contour(X, Y, Z, zdir='z', offset= 0, cmap=cm.jet)
#cset = ax.contour(X, Y, Z, zdir='x', offset=-30, cmap=cm.coolwarm)
#cset = ax.contour(X, Y, Z, zdir='y', offset=30, cmap=cm.coolwarm)

#ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))

cbar = fig.colorbar(surf)#, ticks=(np.arange(0,3500,200)))
#cbar.ax.set_yticklabels(np.arange(0,3500,200))
fig.tight_layout()
plt.savefig('rosenbrock.png', dpi=150)
