#7. Размещаем стандартные текстовые элементы на графике
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))


y = np.arange(0,5,1)
x = np.array([a*a for a in y])
y2 = [0,2,3,4,5,7]
x2= [i+1 for i in y2]
lines = plt.plot(x,y,x2,y2)

plt.minorticks_on()# melkie otmetki
plt.grid(which='major',color = 'grey',linewidth = 2)
plt.grid(which='minor',color = 'g',ls =':')#minornaya setka
plt.show()