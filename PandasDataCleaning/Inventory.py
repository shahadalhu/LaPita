# IMPORT PANDAS
import pandas as pd


# READ FILE
df = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Inventory2.csv')
print(df.head())


# DELETE COLUMNS
df.drop(columns=['Alternate Name',
                 'Price Type',
                 'Price Unit',
                 'Tax Rates',
                 'SKU',
                 'Printer Labels',
                 'Hidden',
                 'Non-revenue item'], inplace=True)
print(df.head())


# DELETE DUPLICATES
print(df.info())
df.drop_duplicates(subset=['Clover ID'], keep='last', inplace=True)
print(df.info())  #5 duplicates found


# EXPORT RECORDS TO CSV
df.to_csv('/Users/shahadalhusain/Desktop/LaPita2/Inventory.csv', index=False)
