#4. Граничные значения осей и локаторы для расположения меток на них
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import IndexLocator,LinearLocator,MultipleLocator

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))#SInusoida

ax.grid()
ax.yaxis.set_major_locator(IndexLocator(base =0.5, offset=0))#shag 0.5 po x
#offset - otstup rizki vpravo
plt.show()
