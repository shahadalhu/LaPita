# IMPORT PANDAS
import pandas as pd


# READ 2022 PAYMENT FILES
df1_payments22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments22-1.csv')
df2_payments22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments22-2.csv')
df3_payments22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments22-3.csv')
df4_payments22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments22-4.csv')

# READ 2023 PAYMENT FILES
df1_payments23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments23-1.csv')
df2_payments23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments23-2.csv')
df3_payments23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments23-3.csv')
df4_payments23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments23-4.csv')
df5_payments23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Payments23-5.csv')


# MERGE ALL RECORDS
df_payments = pd.concat([df1_payments22, df2_payments22, df3_payments22, df4_payments22,
                         df1_payments23, df2_payments23, df3_payments23, df4_payments23,
                         df5_payments23])
print(df_payments.head())


# EXPORT RECORDS TO CSV
df_payments.to_csv('/Users/shahadalhusain/Desktop/LaPita2/Payments.csv', index=False)
