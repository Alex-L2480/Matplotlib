#2. Функция plot для построения и оформления двумерных графиков
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
y = np.arange(0,5,1)
x = np.array([a*a for a in y])
y2 = [0,1,2,3]
x2 = [i+1 for i in y2]
plt.plot(x,y,x2,y2)
plt.grid()#setka
plt.show()