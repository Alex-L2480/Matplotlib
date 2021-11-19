#5. Настраиваем формат отображения меток у координатных осей
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))#SInusoida

ax.yaxis.set_major_formatter(FormatStrFormatter('y = %.2f'))#%d - celye chisla Format otmetok menyaet
#'%f' - float
#'%.2f' - float do sotyh
ax.grid()
plt.show()