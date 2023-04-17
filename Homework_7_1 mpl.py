# Task_1
'''С помощью объектно-ориентированного подхода создайте 4 графика (разместите их в рамках одного изображения)
 установите сетку и легенду для каждого из графиков. для первых 2 графиков(графики А и B)
 используйте рандомно сгенерированные массивы Numpy в качестве данных для осей X и Y.
Графики С и D должны демонстрировать обратную пропорциональность графикам A и B.'''

import matplotlib.pyplot as plt
import numpy as np
import random

fig, axes = plt.subplots(nrows=2, ncols=2)
x_1 = np.linspace(0, 10, 15)
y_1 = np.random.rand(len(x_1))
y_2 = np.random.rand(len(x_1)) * 2
print(x_1, y_1, y_2)
axes[0][0].plot(x_1, y_1, label="A", color='g')
axes[0][0].set_title('График A')
axes[0][0].set_xlabel('Ось X')
axes[0][0].set_ylabel('Ось Y')
axes[0][0].grid(True)
axes[0][0].legend(loc=0)

axes[0][1].plot(x_1, y_2, label="B", color='b')
axes[0][1].set_title('График B')
axes[0][1].set_xlabel('Ось X')
axes[0][1].set_ylabel('Ось Y')
axes[0][1].legend(loc=0)
axes[0][1].grid(True)

axes[1][0].plot(y_1, x_1, label="C", color='g')
axes[1][0].set_title('График C')
axes[1][0].set_xlabel('Ось X')
axes[1][0].set_ylabel('Ось Y')
axes[1][0].legend(loc=0)
axes[1][0].grid(True)

axes[1][1].plot(y_2, x_1, label="D", color='b')
axes[1][1].set_title('График D')
axes[1][1].set_xlabel('Ось X')
axes[1][1].set_ylabel('Ось Y')
axes[1][1].legend(loc=0)
axes[1][1].grid(True)
fig.suptitle("Четыре графика", fontsize=16, color="black")
plt.tight_layout()
plt.show()
