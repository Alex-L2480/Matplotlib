#10. Рисуем гистограммы, столбчатые и круговые диаграммы |
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='lightgrey')
ax = fig.add_subplot()

x = np.arange(10)
y1 = np.random.randint(3,20,len(x))
y2 = np.random.randint(3,15,len(x))
w=0.3
ax.bar(x-w/2,y1,width=w,label='e')#sravnenie stolbcov
ax.bar(x+w/2,y2,width=w+0.1)
ax.legend()
plt.show()
