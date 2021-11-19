#6. Делаем логарифмический масштаб у координатных осей
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi,10*np.pi,0.1)
ax.plot(x,np.sinc(x)*np.exp(-np.abs(x/10)))#Semilogy - bolee detalno chem plot logarifm
ax.set_xscale('symlog',lintresh=2)#kombiniruet lineyniy i logarifmich mashtab
#lintresh =2 znachit v intervale ot -2 do 2 lineyniy mashtab
ax.grid()
plt.show()