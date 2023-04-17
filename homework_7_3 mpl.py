# Task_3
""" По ссылке ниже находятся результаты эксперимента для определения оценки плотности и частоты столкновений электронов
в плазме газового разряда.
https://docs.google.com/spreadsheets/d/1uhfKZNivSHeENrM4Go8n0KMs9jYQeLKtPJTju7HqQXg/edit#gid=777647444
Назвать график, обозначить оси, рассчитать среднеквадратичное отклонение, построить график и сохранить его в формате jpeg."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data - Лист1.csv')
X = df["X"]
Y = df["Y"]
arr = np.array([X, Y]).transpose()

st_d = np.std(arr)
print(st_d)
plt.plot(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График')
plt.savefig('test_3.jpeg')
