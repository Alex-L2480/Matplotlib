#10. Рисуем гистограммы, столбчатые и круговые диаграммы |
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

y = np.random.normal(0,2,500)
ax.hist(y,20)#histogramma  20 - kolich intervalov
ax.grid()

plt.show()
