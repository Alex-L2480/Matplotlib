#8. Добавляем легенду и рисуем геометрические фигуры на графиках
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

x = np.arange(-2*np.pi,2*np.pi,0.1)
cos = Line2D(x,np.cos(x))# cosinusoida kak figura

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

ax.add_line(cos)#dobavlenie linii
ax.set(xlim=(-4,4),ylim=(-4,4))#granichnye znachenia

plt.show()