#2. Функция plot для построения и оформления двумерных графиков
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
y = np.random.randint(1,10,5)
x = np.random.randint(1,10,5)
plt.plot(x,y)#sam grafik
plt.show()