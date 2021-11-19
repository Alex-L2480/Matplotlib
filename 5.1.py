#5. Настраиваем формат отображения меток у координатных осей
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))#SInusoida

ax.set_xticklabels([])#skravayut otmetki
ax.set_yticklabels([])
ax.grid()
plt.show()