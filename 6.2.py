#6. Делаем логарифмический масштаб у координатных осей
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi,10*np.pi,0.5)
ax.plot(x,np.sinc(x)*np.exp(-np.abs(x/10)))#Semilogy - bolee detalno chem plot logarifm
ax.set_yscale('log')#po osi y log mashtab metod
#base = 5 osnovanie log mozhno dobavit
ax.grid()
plt.show()