#6. Делаем логарифмический масштаб у координатных осей
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi,10*np.pi,0.5)
ax.plot(x,np.sinc(x)*np.exp(-np.abs(x/10)))#Semilogy - bolee detalno chem plot logarifm
ax.set_yscale('log',basey = 10, subsy=[2,9])#subsy - melkie otmetki
#basey = 5 osnovanie log mozhno dobavit
ax.grid()
plt.show()