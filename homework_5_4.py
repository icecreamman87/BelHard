'''Запросить у пользователя данные (имя, фамилия, возраст) и создать файл с этими значениями.
'''

import pandas as pd
df = pd.DataFrame([[input("Введите имя:"), input("Введите фамилию:"), input("Введите возраст:")]], columns = ['name', 'surname',\
'age'])
print(df)