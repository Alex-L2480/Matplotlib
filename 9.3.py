#9. Рисуем ступенчатые, стековые, stem и точечные графики

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

x = np.arange(0,10)
ax.step (x,x,'-o',x,np.cos(x),'--x')# stupenchaty grafik 2 grafika
ax.grid()

plt.show()