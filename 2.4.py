#2. Функция plot для построения и оформления двумерных графиков
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
y = np.arange(0,5,1)
x = np.array([a*a for a in y])
a = plt.plot(x,y,'--')# 3 parametr tip linii
print(a)
plt.setp(a,linestyle=':')# ustanovka svoystv
plt.grid()#setka
plt.show()