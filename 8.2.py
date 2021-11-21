#8. Добавляем легенду и рисуем геометрические фигуры на графиках
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

line1, = ax.plot(np.arange(0,5,0.25),'--ob',label = 'line1')#legenda
line2, = ax.plot(np.arange(0,10,0.5),label ='line2')# zapyataya nuzhna

ax.legend((line2,line1),['Линия2','Линия1'],loc ='upper right')#vyzov legendy
#loc - mestopolozh legendy
plt.show()