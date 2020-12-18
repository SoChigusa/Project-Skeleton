import numpy as np
import matplotlib.pyplot as plt

# figure settings
fig = plt.figure()

# arbitrary aspect ratio
# fig = plt.figure(figsize=[4,2.25])

# subfigure
ax = fig.add_subplot(1,1,1)
# ax2= fig.add_subplot(2,2,1)

# data input
# data = np.loadtxt('file name', usecols=range(3), delimiter='\t', skiprows=1)
# x = data[:,0]
# y = data[:,1]
# z = data[:,2]

# line plot
# ax.plot(x, y, color='r', linestyle='-', linewidth=2, label='hoge')

# reshape 1D to 2D if necessary
# x,y,z = x.reshape(ny,nx), y.reshape(ny,nx), z.reshape(ny,nx)

# contour plot (line / area)
# cs = ax.contour(x, y, z, levels=[z1, z2, z3], colors='b', linestyles='-')
# ax.contourf(x, y, z, levels=[zmin,zmax], alpha=0.3, colors='gray')

# contour legend
# h,_   = cs.legend_elements()
# ax.legend([h[0]], ['legend'], fontsize=20)

# contour small label
# ax.clabel(cs, fmt='%d')

# histogram
# ax.hist(x, bins=nbin, range=(xmin, xmax), color='m', ec='black', label='legend')

# log plot
# ax.set_xscale('log')
# ax.set_yscale('log')

# plot range
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# ticks setting
# ax.set_xticks([0, 0.5, 1])
# ax.set_yticks([0, 0.5, 1])
ax.tick_params(labelsize=15)

# figure captions
ax.set_title('Empty Title', size=20)
ax.set_xlabel('Empty x-label', size=15)
ax.set_ylabel('Empty y-label', size=15)
# ax.legend(fontsize=15, loc='best')

plt.tight_layout()
plt.savefig('figure/tmp.pdf', bbox_inches='tight')
