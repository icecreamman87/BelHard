# Task_2
# """Вычислить среднее значение колонки Temperature и добавить новую колонку delta_T, в которой хранится модуль разности
#  текущей Temperature и средней. Проверить содержит ли датафрейм NaN значения.
#   Вычислить максимальное значение Temperature. Вернуть датафрейм в котором delta_T <= Tmax/2 и Temperature >= delta_Tmin.
#   Полученный датафрейм сохранить в формате CSV.
import pandas as pd

df = pd.read_csv("6 class csv.csv")
T_avr = df['Temperature (K)'].mean()
print(f"Cреднее значение Temperature = {T_avr}")
df["delta_T"] = abs(df["Temperature (K)"] - T_avr)
print(df)
num_nan = df.isnull().sum()
print(num_nan)
T_max = df["Temperature (K)"].max()
delta_Tmin = df["delta_T"].min()
new_df = df[(df["delta_T"] <= T_max / 2) & (df["Temperature (K)"] >= delta_Tmin)]
print(new_df)
file_2 = new_df.to_csv("csv_new_df")
print(file_2)
