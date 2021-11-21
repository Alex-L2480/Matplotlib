#8. Добавляем легенду и рисуем геометрические фигуры на графиках
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import * #import vseh figur

rect = Rectangle((0,0),2.5,0.5,facecolor ='b')#pryamougolnik
e = Ellipse((-3,1),2,3,facecolor = 'g')#ellips

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

ax.add_patch(rect)#dobavlenie pryamoug
ax.add_patch(e)
ax.set(xlim=(-4,4),ylim=(-4,4))#granichnye znachenia

plt.show()