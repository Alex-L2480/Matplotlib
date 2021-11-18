#2. Функция plot для построения и оформления двумерных графиков
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
y = np.arange(0,5,1)
x = np.array([a*a for a in y])
y2 = [0,1,2,3]
x2 = [i+1 for i in y2]
a = plt.plot(x,y,'--ro',x2,y2,':gs',markerfacecolor='w')# r - red g - green #o-kruglye tochki s - kvadratnye
plt.setp(a[0],linestyle='-.',marker ='s',markerfacecolor='b',linewidth=4,alpha=0.5)# ustanovka svoystv
plt.grid()#setka
plt.show()