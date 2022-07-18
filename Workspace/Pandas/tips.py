import numpy as np
import pandas as pd

df_csv = pd.read_csv('.\DATA\\tips.csv')
print(df_csv)
print(df_csv.columns)
print(df_csv.index)

print(df_csv.head())
print(df_csv.head(3))
print(df_csv.tail())
print(df_csv.tail(3))

print(df_csv.info())
print(df_csv.describe())
print(df_csv.describe().transpose()) # stats of values in df

print(df_csv[['total_bill', 'tip']])
df_csv['tip_percentage'] = 100 * df_csv['tip'] / df_csv['total_bill']
print(df_csv['tip_percentage'])

df_csv['price_per_person'] = np.round(df_csv['total_bill'] / df_csv['size'], 2)
print(df_csv['price_per_person'])

#df_csv.drop('tip_percentage', axis=1)

print(df_csv.index)

df_csv['tip_percentage'] = 100 * df_csv['tip'] / df_csv['total_bill']
df_csv['price_per_person'] = np.round(df_csv['total_bill'] / df_csv['size'], 2)
df_csv = df_csv.set_index('Payment ID')

# df_csv.reset_index()

print(df_csv.iloc[0]) # location
print(df_csv.loc['Sun2959']) # index