#5. Настраиваем формат отображения меток у координатных осей
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))#SInusoida

ax.xaxis.set_major_formatter(NullFormatter())#skravaet otmetki po x

ax.grid()
plt.show()