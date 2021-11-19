#6. Делаем логарифмический масштаб у координатных осей
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi,10*np.pi,0.1)
ax.loglog(x,np.sinc(x)*np.exp(-np.abs(x/10)))#log na obe osi


ax.grid()
plt.show()