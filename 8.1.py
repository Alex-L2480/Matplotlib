#8. Добавляем легенду и рисуем геометрические фигуры на графиках
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

ax.plot(np.arange(0,5,0.25),'--ob',label = 'line1')#legenda
ax.plot(np.arange(0,10,0.5),label ='line2')

ax.legend()#vyzov legendy

plt.show()