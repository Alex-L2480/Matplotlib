#5. Настраиваем формат отображения меток у координатных осей
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x)*1e5)#SInusoida

sf = ScalarFormatter()#peremennaya ssylaetsya na ekzemplyar klassa
sf.set_powerlimits((-4,4))# predely otobrazhenia stepeney
ax.yaxis.set_major_formatter(sf)# 

ax.grid()
plt.show()