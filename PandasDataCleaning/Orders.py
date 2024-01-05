# IMPORT PANDAS
import pandas as pd


# READ FILE
df = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita2/Orders.csv')
print(df.head())


# DELETE COLUMNS
df.drop(columns=['Order Date',
                 'Invoice Number',
                 'Order Employee Name',
                 'Order Employee Custom ID',
                 'Note',
                 'Currency',
                 'Tip',
                 'Service Charge',
                 'Payment Note',
                 'Refunds Total',
                 'Manual Refunds Total',
                 'Credit Card Auth Code',
                 'Credit Card Transaction ID',
                 'Order Type'], inplace=True)
print(df.head())


# DELETE OPEN PAYMENTS IN ORDER PAYMENT STATE COLUMN
print(df.info())
for x in df.index:
    if df.loc[x, 'Order Payment State'] == 'Open':
        df.drop(x, inplace=True)
print(df.info())


# DELETE DUPLICATES
# keep most recent instance
print(df.info())
df.drop_duplicates(subset=['Order ID'], keep='last', inplace=True)
print(df.info())


# CHANGE DATATYPE
#df['Order Number'] = df['Order Number'].astype('int64')


# EXPORT RECORDS TO CSV
df.to_csv('/Users/shahadalhusain/Desktop/LaPita2/Orders.csv', index=False)
