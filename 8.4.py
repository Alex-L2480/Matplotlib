#8. Добавляем легенду и рисуем геометрические фигуры на графиках
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

l1 = Line2D([1,2,3],[1,2,4])#koordinaty lomanoy linii

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

ax.add_line(l1)#dobavlenie linii
ax.set(xlim=(1,3),ylim=(1,5))#granichnye znachenia

plt.show()