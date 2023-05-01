import pandas as pd
import numpy as np

df = pd.read_excel('Payment data.xlsx')
print(df)
print(df.ApplicationType.unique())
df = df.drop((df.query('ApplicationType == "Prepayment"').index))
df = df.drop((df.query('ApplicationType == "DEPOSIT"').index))
df = df.dropna(axis=1, how='all')
df[['Created By', 'Department', 'Payment Terms', 'Project Code', 'Header Reamark', 'Approval Method',
    'AuthorizedDepartment', 'Category', 'Invoice Date', 'Invocie Status', 'Exchange Rate', 'Invoice No.']] = \
    df[['Created By', 'Department', 'Payment Terms', 'Project Code', 'Header Reamark', 'Approval Method',
        'AuthorizedDepartment', 'Category', 'Invoice Date', 'Invocie Status', 'Exchange Rate', 'Invoice No.']].fillna(
        'unknown')
df["Quantity"] = df["Quantity"].fillna('q-ty by amount')
df["Tax Rate"] = df["Tax Rate"].fillna('without VAT')
df["Supplier"] = df["Supplier"].apply(lambda x: "unknown" if "null" in x else x)
t = 0.00013
df['Applied Total Amount'] = np.where(df['Head Currency'] == 'BYR', df['Applied Total Amount'] * t,
                                      df['Applied Total Amount'])
df['Head Currency'] = df['Head Currency'].replace("BYR", "BYN")
df_2 = df.drop(columns=['Sub ApplicationType', 'Purchasing Process', 'Status', 'Owner Group', 'Company', 'Region',
                        'RepOffice', 'FinLocation', 'Deposit Type', 'Supplier Site', 'Payment Method',
                        'Tax Afford Method',
                        'Sub Project Code', 'Project', 'Accepter', 'Supervisor', 'Authorized Approver', 'Submit Date',
                        'Last Approve Date',
                        'Line No.', 'line Description', 'Column', 'COA Account Combination', 'Invoice Currecny',
                        'Invoice Amount（Excul Tax）', 'Invoice Amount（Incl Tax）', 'Tax Code', 'Tax Product',
                        'Converted Amount(a*b)', 'Purchasing Contract No.', 'Invoice Date'], axis=1)
df_2.rename(columns={'Creation Date': 'Payment Date'}, inplace=True)
print(df_2)
file = df_2.to_excel('pd_upd.xlsx')
print(file)

df = pd.read_excel('pd_upd.xlsx', index_col=0)
print(df.rename_axis("N", axis='columns'))
print(df["Exchange Rate"].value_counts())
print(df.dtypes)
df["Exchange Rate"] = df["Exchange Rate"].apply(lambda x: x / 10000 if x > 1000 else x)
print(df["Exchange Rate"].value_counts())
print(df.groupby('Head Currency').ApplicationType.count())
df.rename(columns={'Applied Total Amount': 'Payment_amount'}, inplace=True)
print(df.groupby(['Head Currency']).Payment_amount.agg([len, min, max]))
print(df.groupby(['Head Currency']).Payment_amount.mean())
print(df.loc[df['Payment_amount'].idxmax(), 'Header Reamark'])
print(df.loc[df['Payment_amount'].idxmax(), 'Payment Date'])
print(df.groupby('Supplier').Payment_amount.count().sort_values(ascending=False))
rates = {'BYN': 1, 'RUB': 0.036, 'USD': 2.93, 'EUR': 3.2}


def convert_currency(row):
    currency = row['Head Currency']
    rate = rates[currency]
    amount_BYN = row['Payment_amount'] * rate
    return amount_BYN


df['amount_BYN'] = df.apply(convert_currency, axis=1)
print(f"Средний размер платежа = {df.amount_BYN.sum() / df.amount_BYN.count()}")
print(df.groupby(['Supplier']).amount_BYN.sum().sort_values(ascending=False).astype(str))
print(df.groupby(['Supplier']).amount_BYN.mean().sort_values(ascending=False))
water = df['Header Reamark'].map(lambda desc: "water" in desc).sum()
milk = df['Header Reamark'].map(lambda desc: "milk" in desc).sum()
coffee = df['Header Reamark'].map(lambda desc: "coffee" in desc).sum()
goods_counts = pd.Series([water, milk, coffee], index=["water", "milk", "coffee"])
print(goods_counts)
df['Payment Date'] = pd.to_datetime(df['Payment Date'])
df['year'] = df['Payment Date'].dt.year
df['month'] = df['Payment Date'].dt.month
df['year_month'] = df['year'].map(str) + '_' + df['month'].map(str)
new_df = df.groupby('year_month')['amount_BYN'].sum().reset_index()
print(new_df)
file_date = new_df.to_excel("Date_payments.xlsx")
print(file_date)
print(df.groupby('year_month')['amount_BYN'].sum().sort_values(ascending=False).reset_index().astype(str))
print(df.groupby('year_month')['ApplicationType'].count().sort_values(ascending=False).reset_index().astype(str))
print(df.groupby('year')['amount_BYN'].sum().sort_values(ascending=False).reset_index().astype(str))
