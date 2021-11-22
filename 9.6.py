#9. Рисуем ступенчатые, стековые, stem и точечные графики

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

x = np.random.normal(0,2,500)
y = np.random.normal(0,2,500)

ax.scatter(x,y)# tochecnyi garfik

ax.grid()

plt.show()