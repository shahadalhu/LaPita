# IMPORT PANDAS
import pandas as pd


# READ FILE
df = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/SalesPerMonth.csv')
print(df.head())


# DELETE COLUMNS
df.drop(columns=['Non-revenue Items',
                 'Gift Card Activations',
                 'Tips',
                 'Service Charges'], inplace=True)
print(df.head())


# EXPORT RECORDS TO CSV
df.to_csv('/Users/shahadalhusain/Desktop/LaPita2/SalesPerMonth.csv', index=False)
