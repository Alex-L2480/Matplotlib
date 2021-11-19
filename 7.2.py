#7. Размещаем стандартные текстовые элементы на графике
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4),facecolor='b')
ax = fig.add_subplot()

plt.figtext(0.05,0.6,'Textttttttttt',color='r',fontsize = 12)#text v oblasti okna s koordinatami
fig.suptitle('Zagolovok')

ax.set_xlabel('Ox')#podpisi dlya osey
ax.set_ylabel('Oy')
ax.set(facecolor='lightgrey')# eshe 1 variant dobavit parametr

ax.text(0.05,0.2,'Proizvolniy text',fontsize = 15,bbox={'boxstyle':'round','facecolor':'g'})# vnutri osey
#bbox - svoystva okruzhenia texta
ax.annotate('Annotation',xy=(0.2,0.4),xytext = (0.6,0.7),arrowprops={'facecolor':'gray','shrink':0.1})
# strelka ukazatel
plt.show()