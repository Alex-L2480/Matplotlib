#9. Рисуем ступенчатые, стековые, stem и точечные графики

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

x = np.arange(0,10)
ax.step (x,x,'-go',where = 'post')# stupenchaty grafik , svoystva...post - tochki v vershine vertikali
ax.grid()

plt.show()