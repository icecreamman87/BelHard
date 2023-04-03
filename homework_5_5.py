'''Напишите программу, которая будет открывать определенный файл file и выводить на печать построчно
 последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
'''

import pandas as pd
df = pd.read_csv('D:\GP\R&D July 2022\Data science\Lesson 5 - Файлы и pandas\wholesale-trade-survey-september-2022-quarter-csv.csv')
print(df.tail(int(input("Введите количество lines "))))