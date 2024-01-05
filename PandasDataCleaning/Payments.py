# IMPORT PANDAS
import pandas as pd


# READ FILE
df = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita2/Payments.csv')
print(df.head())


# DELETE COLUMNS
df.drop(columns=['External Payment ID',
                 'Invoice Number',
                 'Card Auth Code',
                 'Transaction #',
                 'Note',
                 'Tender',
                 'Card Brand',
                 'Card Number',
                 'Card Entry Type',
                 'Currency',
                 'Amount',
                 'Tax Amount',
                 'Tip Amount',
                 'Service Charge Amount',
                 'Payment Employee ID',
                 'Payment Employee Name',
                 'Payment Employee Custom ID',
                 'Order Date',
                 'Order Employee ID',
                 'Order Employee Name',
                 'Order Employee Custom ID',], inplace=True)
print(df.head())


# DELETE FAILED PAYMENTS IN RESULT COLUMN
print(df.info())

for x in df.index:
    if df.loc[x, 'Result'] == 'FAIL':
        df.drop(x, inplace=True)

print(df.info())


# REPLACE NULL VALUES
df['# Refunds'] = df['# Refunds'].fillna(0)
df['Refund Amount'] = df['Refund Amount'].fillna(0.00)


# CHANGE DATATYPE
df['# Refunds'] = df['# Refunds'].astype('int64')


# PAYMENT DATE COLUMN
# 1- replace EDT/EST with whitespace
df['Payment Date'] = df['Payment Date'].str.replace(' EDT', '')
df['Payment Date'] = df['Payment Date'].str.replace(' EST', '')

# 2- convert string to datetime
df['Payment Date'] = pd.to_datetime(df['Payment Date'], utc=False, format='%d-%b-%Y %I:%M %p')

# 3- sort by date ASC
df = df.sort_values(by=["Payment Date"], ascending=True)

print(df.dtypes)
print(df.head())


# DELETE DUPLICATES
# keep most recent instance
print(df.info())
df.drop_duplicates(subset=['Payment ID'], keep='last', inplace=True)
print(df.info())


# EXPORT RECORDS TO CSV
df.to_csv('/Users/shahadalhusain/Desktop/LaPita2/Payments.csv', index=False)
