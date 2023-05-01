import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_excel("Date_payments.xlsx")

p = 2
d = 1
q = 2
model = ARIMA(df['amount_BYN'], order=(p, d, q)).fit()
fcst = model.forecast(steps=12)
print(fcst)
df_plan = fcst.to_excel("Plan.xlsx")
print(df_plan)
df_plan = pd.read_excel("Plan.xlsx", index_col=0)
new_column_values = ['2023_5', '2023_6', '2023_7', '2023_8', '2023_9', '2023_10', '2023_11', '2023_12', '2024_1',
                     '2024_2', '2024_3', '2024_4']
df_plan.insert(0, 'year_month', new_column_values)
df_plan.rename(columns={'predicted_mean': 'amount_BYN'}, inplace=True)
print(df_plan.amount_BYN.sum())
print(df_plan)
file = df_plan.to_excel("Date_payments_plan.xlsx")
print(file)

fig, ax = plt.subplots()
ax.plot(df['year_month'], df['amount_BYN'], label='Исторические данные', marker='o')
ax.plot(df_plan['year_month'], df_plan['amount_BYN'], label='Прогнозируемые данные', linestyle='--')
ax.legend()
ax.set_xlabel('year_month')
plt.xticks(rotation=90,fontsize=8)
ax.set_ylabel('amount_BYN')
ax.set_title('График исторических и прогнозируемых данных')
plt.savefig('Month_payments_plan.jpeg')

df_grouped = df.groupby(df['year_month'].str.split('_').str[0])['amount_BYN'].sum()
print(df_grouped.astype(str))
df_grouped_plan = df_plan.groupby(df_plan['year_month'].str.split('_').str[0])['amount_BYN'].sum()
print(df_grouped_plan.astype(str))
plt.plot(df_grouped.index, df_grouped.values, label='Исторические данные')
plt.plot(df_grouped_plan.index, df_grouped_plan.values, label='Прогнозируемые данные')
plt.title('График исторических и прогнозируемых закупок')
plt.xlabel('Год')
plt.ylabel('Закупки, BYN')
plt.legend()
plt.savefig('Year_payments_plan.jpeg')
