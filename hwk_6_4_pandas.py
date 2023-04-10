# Task_4
# """Для каждого спектрального класса вычислить дисперсию для Luminosity(L/Lo), стандартная ошибка среднего для Absolute magnitude(Mv)
# и среднеквадратичное отклонение для Temperature. На основе данных создать датафрейм и записать в excel файл."""
#
import pandas as pd

df = pd.read_csv("6 class csv.csv")
new_df_1 = ["Spectral Class", "Luminosity(L/Lo)"]
group_data_1 = df[new_df_1].groupby("Spectral Class")
print(group_data_1.var())
print()
new_df_2 = ["Spectral Class", "Absolute magnitude(Mv)"]
group_data_2 = df[new_df_2].groupby("Spectral Class")
print(group_data_2.sem())
print()
new_df_3 = ["Spectral Class", "Temperature (K)"]
group_data_3 = df[new_df_3].groupby("Spectral Class")
print(group_data_3.std())
result_df = pd.concat([group_data_1.var(), group_data_2.sem(), group_data_3.std()], axis=1)
print(result_df)
file_3 = result_df.to_excel("result_excel_df.xlsx")
print(file_3)