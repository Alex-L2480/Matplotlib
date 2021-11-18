#3. Отображение нескольких координатных осей в одном окне | Matplotlib уроки
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

f1 = plt.figure(figsize=(3,3))#eshe 1 figura
axx1 = f1.add_subplot(121)#добавление сублот
axx1.plot(np.arange(0,5,0.2))

f , ax = plt.subplots(2,3)# sozdanie pustyh osey v figure
f.set_size_inches(7,7)#razmer figury
f.set_facecolor('g')#cvet figury

ax[0,0].plot(np.arange(0,5,0.2))#osi koord 0 0
ax[0,0].grid()
ax[0,1].plot(np.arange(2,4,0.1))#osi koord 0 1
ax[0,1].grid()


plt.show()