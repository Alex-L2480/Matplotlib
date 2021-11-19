#5. Настраиваем формат отображения меток у координатных осей
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["axes.formatter.limits"] = (-4,4)## predely otobrazhenia stepeney na osyah
#esli nuzhno dlya vseh grafikov
fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x)*1e5)#SInusoida

ax.grid()
plt.show()