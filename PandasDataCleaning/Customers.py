# IMPORT PANDAS
import pandas as pd


# READ FILE
df = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Customers2.csv')
print(df.head())


# DELETE COLUMNS
df.drop(columns=['Address Line 1',
                 'Address Line 2',
                 'Address Line 3',
                 'City',
                 'State / Province',
                 'Postal / Zip Code',
                 'Country',
                 'Additional Addresses'], inplace=True)
print(df.head())


# PAYMENT DATE COLUMN
# 1- replace EDT/EST with whitespace
df['Customer Since'] = df['Customer Since'].str.replace(' EDT', '')
df['Customer Since'] = df['Customer Since'].str.replace(' EST', '')

# 2- convert string to datetime
df['Customer Since'] = pd.to_datetime(df['Customer Since'], utc=False, format='%d-%b-%Y %I:%M %p')

# 3- sort by date ASC
df = df.sort_values(by=["Customer Since"], ascending=True)
print(df.dtypes)
print(df.head())


# DELETE DUPLICATES
# keep first instance for oldest record
print(df.info())
df.drop_duplicates(subset=['Customer ID'], keep='first', inplace=True)
print(df.info())  # no duplicates found


# EXPORT RECORDS TO CSV
df.to_csv('/Users/shahadalhusain/Desktop/LaPita2/Customers.csv', index=False)
