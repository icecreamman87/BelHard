'''Создать и прочитать CSV файл с помощью Pandas. PLot box посмотрел дополнительно
'''

import pandas as pd
import csv
df = pd.read_csv('D:\GP\R&D July 2022\Data science\Lesson 5 - Файлы и pandas\wholesale-trade-survey-september-2022-quarter-csv.csv',sep=",")
print(df)
print(df.head())
import matplotlib
import matplotlib.pyplot as plt
df.plot.box()
print(plt.show())