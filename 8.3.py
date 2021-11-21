#8. Добавляем легенду и рисуем геометрические фигуры на графиках
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

l1 = Line2D([1,2,3],[1,2,4])#koordinaty lomanoy linii

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

line1, = ax.plot(np.arange(0,5,0.25),'--ob',label = 'line1')#legenda
line2, = ax.plot(np.arange(0,10,0.5),label ='line2')# zapyataya nuzhna

ax.add_line(l1)#dobavlenie linii
plt.show()