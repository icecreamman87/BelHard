# Task 1
"""Получить подробную информацию о датафрейме (count, mean, std, min, 25%, 50%, 75%, max).
Полученный датафрейм транспонировать. Также вывести список колонок датафрейма и информацию о типах данных колонок датафрейма.
На основе полученной информации создать датафрейм и записать его в формате JSON.
"""
import pandas as pd

df = pd.read_csv("6 class csv.csv")
print(df.describe())
print(df.transpose())
print(df.columns)
new_df = pd.DataFrame(
    {"Temperature (K)": [], "Luminosity(L/Lo)": [], "Radius(R/Ro)": [], 'Absolute magnitude(Mv)': [], 'Star type': [],
     'Star color': [], 'Spectral Class': []})
print(new_df)
file_1 = new_df.to_json("json_new_df")
print(file_1)
