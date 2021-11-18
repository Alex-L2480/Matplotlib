import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator,LinearLocator,MultipleLocator

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))#SInusoida


ax.minorticks_on()#minor grid
ax.grid(which='major',lw=2)
ax.grid(which='minor')
ax.xaxis.set_minor_locator(MaxNLocator(3))#maksimum rizok dlya udobnogo prosmotra

plt.show()
