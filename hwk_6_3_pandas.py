# Task_3
# """Вычислить коэффициент корреляции датафрейма. Вычислить среднее значение Absolute magnitude(Mv) для каждого Star type.
# Вычислить количество записей для каждого спектрального класса."""

import pandas as pd

df = pd.read_csv("6 class csv.csv")
print(df.corr())
new_df = ["Star type", "Absolute magnitude(Mv)"]
group_data = df[new_df].groupby("Star type")
print(group_data.mean())
print()
print(df.groupby("Spectral Class").count())
