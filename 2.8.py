#2. Функция plot для построения и оформления двумерных графиков
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
x = np.arange(-2*np.pi,2*np.pi,0.1)
y = np.cos(x)
plt.plot(x,y)
plt.fill_between(x,y,where=(y<0),color='r')#zakrashivaet
plt.fill_between(x,y,where=(y>0),color='b')# uslovia
plt.grid()#setka
plt.show()