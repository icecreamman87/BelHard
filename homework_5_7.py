'''Перевести csv файл в json'''

import pandas as pd
df = pd.read_csv('D:\GP\R&D July 2022\Data science\Lesson 5 - Файлы и pandas\wholesale-trade-survey-september-2022-quarter-csv.csv')
df.to_json('D:\GP\R&D July 2022\Data science\Lesson 5 - Файлы и pandas\wholesale-trade-survey-september-2022-quarter-csv.json')
print(df.info())