#3. Отображение нескольких координатных осей в одном окне | Matplotlib уроки
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
ax1 = plt.subplot(1,3,1)#delit okno na chasti
plt.plot(np.random.random(10))
ax2 = plt.subplot(1,3,2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(1,3,3)
a = np.random.random(10)
print(a)
plt.plot(a)
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()
