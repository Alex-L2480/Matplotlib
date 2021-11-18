#4. Граничные значения осей и локаторы для расположения меток на них
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
ax.plot(np.arange(1,5,0.25))

ax.grid()
ax.xaxis.set_major_locator(NullLocator())#setka tolko po y

plt.show()
