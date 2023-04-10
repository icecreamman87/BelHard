# Task_5
'''Будет CSV файл с набором измерений.
Нужно рассчитать дисперсию, среднеквадратичное отклонение, отобразить гистограмму и решить задачу поиска наименьших квадратов.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("6 class csv.csv")
v = np.var(df["Temperature (K)"])
st_d = np.std(df["Temperature (K)"])
print(f"Дисперсия = {v},CРОТКЛ = {st_d}")

x = df['Spectral Class']
y = df['Temperature (K)']
plt.plot(x, y)
plt.xlabel('Спектральный класс')
plt.ylabel('Температура (К)')
plt.title('Температура звезд в зависимости от их класса')
plt.show()
