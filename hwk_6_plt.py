'''Считать данные из csv файла.
Назвать график, обозначить оси, рассчитать среднеквадратичное отклонение, построить график и сохранить его в формате jpeg.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Book1.csv')
print(df)

X = df["X"]
Y = df["Y"]
data = np.array([X, Y]).transpose()
st_d = np.std(data)
print(f"Среднеквадратическое отклонение = {st_d}")
plt.plot(X, Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График')
plt.savefig('test_2.jpeg')
