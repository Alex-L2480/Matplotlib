#2. Функция plot для построения и оформления двумерных графиков
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
y = np.arange(0,5,1)
x = np.array([a*a for a in y])
plt.plot(x,y)
plt.grid()#setka
plt.show()
