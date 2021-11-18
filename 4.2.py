#4. Граничные значения осей и локаторы для расположения меток на них
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
ax.plot(np.arange(1,5,0.25))

ax.set_xlim(-10,25)#granichnye znacheniya osey
ax.set_ylim(-2,7)
plt.show()
