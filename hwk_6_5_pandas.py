# Task_5
"""На основании датасета df создать новый датафрейм new_df с двумя колонками Temperature и temperature_C, где
new_df["Temperature"] = df["Temperature"]
а в колонке temperature_C хранится значение температуры в С.
Соединить два датафрейма в один, как минимум тремя разными способами.
После соединения проверить датафрейм на наличие NaN значений. Заменить отсутствующие данные следующими способами:
Для всех NaN значений установить среднее значение столбца.
Заменить NaN значения с помощью интерполяции.
Удалить строки содержащие NaN значения."""
import pandas as pd

df = pd.read_csv("6 class csv.csv")
To = 273.15
df["temperature_C"] = df["Temperature (K)"] - To
# Variant_1
new_df_v1 = ["Temperature (K)", "temperature_C"]
print(df[new_df_v1])
# Variant_2
new_df_v2 = pd.concat([df["Temperature (K)"], df["temperature_C"]], axis=1)
print(new_df_v2)
# Variant_3
new_df_v3 = pd.merge(df["Temperature (K)"], df["temperature_C"], left_index=True, right_index=True)
print(new_df_v3)
num_nan = new_df_v3.isnull().sum()
print(num_nan)

# Task_5_1
import pandas as pd

df = pd.read_excel("NaN_df.xlsx")
num_nan = df.isnull().sum()
print(num_nan)
# Variant_1
df["Temperature (K)"] = df["Temperature (K)"].fillna(df["Temperature (K)"].mean())
df["temperature_C"] = df["temperature_C"].fillna(df["temperature_C"].mean())
print(df.loc[10:60])
# Variant_2
df["Temperature (K)"] = df["Temperature (K)"].interpolate()
df["temperature_C"] = df["temperature_C"].interpolate()
print(df.loc[10:60])
# Variant_3
df = df.dropna(axis=0)
print(df)
print(df.loc[10:60])
