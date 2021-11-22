#10. Рисуем гистограммы, столбчатые и круговые диаграммы |
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

vals = [10,40,23,30,7]#doli
labels = ['toyota','bmw','lexus','audi','lada']#metki
ax.pie(vals,labels = labels,wedgeprops=dict(width=0.5))#krugovaya diagramma
#wedgeprops - kolco
plt.show()