#3. Отображение нескольких координатных осей в одном окне | Matplotlib уроки
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

f , ax = plt.subplots(2,3)# sozdanie pustyh osey v figure
ax[0,0].plot(np.arange(0,5,0.2))#osi koord 0 0
ax[0,0].grid()

plt.show()