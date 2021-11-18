#3. Отображение нескольких координатных осей в одном окне | Matplotlib уроки
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
fig  = plt.figure(figsize=(7,4))
gs = GridSpec(ncols=3,nrows=2,figure=fig)#delit figuru 

ax1 = plt.subplot(gs[0,0])#funkcia
ax1.plot(np.arange(0,5,0.1))
ax2 = fig.add_subplot(gs[1,0:2])
ax2.plot(np.random.randint(1,10,5))#metod
ax2 = fig.add_subplot(gs[:,2])
ax2.plot(np.random.randint(1,10,5))

plt.show()