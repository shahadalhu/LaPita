# IMPORT PANDAS
import pandas as pd

# READ 2022 ORDER FILES
df1_orders22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders22-1.csv')
df2_orders22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders22-2.csv')
df3_orders22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders22-3.csv')
df4_orders22 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders22-4.csv')

# READ 2023 ORDER FILES
df1_orders23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders23-1.csv')
df2_orders23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders23-2.csv')
df3_orders23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders23-3.csv')
df4_orders23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders23-4.csv')
df5_orders23 = pd.read_csv('/Users/shahadalhusain/Desktop/LaPita1/Orders23-5.csv')

# MERGE ALL RECORDS
df_orders = pd.concat([df1_orders22, df2_orders22, df3_orders22, df4_orders22,
                       df1_orders23, df2_orders23, df3_orders23, df4_orders23,
                       df5_orders23])
print(df_orders.head())


# EXPORT RECORDS TO CSV
df_orders.to_csv('/Users/shahadalhusain/Desktop/LaPita2/Orders.csv', index=False)
