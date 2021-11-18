#3. Отображение нескольких координатных осей в одном окне | Matplotlib уроки
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


f , ax = plt.subplots()# sozdanie pustyh osey v figure
f.set_size_inches(7,7)#razmer figury
f.set_facecolor('g')#cvet figury

ax.plot(np.arange(0,5,0.2))#osi koord 0 0

ax.plot(np.arange(2,4,0.1))#osi koord 0 1



plt.show()