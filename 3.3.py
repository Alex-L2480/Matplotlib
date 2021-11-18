#3. Отображение нескольких координатных осей в одном окне | Matplotlib уроки
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
ax1 = plt.subplot(231)#delit okno na chasti
plt.plot(np.random.random(10))
ax2 = plt.subplot(232)
plt.plot(np.random.random(10))
ax3 = plt.subplot(233)
plt.plot(np.random.random(10))
ax4 = plt.subplot(212)
plt.plot(np.random.random(10))
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
