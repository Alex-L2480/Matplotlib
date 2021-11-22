#9. Рисуем ступенчатые, стековые, stem и точечные графики

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

x = np.arange(-np.pi,np.pi,0.3)
ax.stem(x,np.cos(x),bottom=0.5)# stem -  grafik is tochek na vertikalyah s bazovym urovnem na 0
#bottom - bazovyi uroven
ax.grid()

plt.show()