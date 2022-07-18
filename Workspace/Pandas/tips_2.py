import numpy as np
import pandas as pd

df = pd.read_csv('.\DATA\\tips.csv')

#bool_series = df['total_bill'] > 40
#df[bool_series]

# conditional Filtering
#df[df['total_bill'] > 40]
#df[df['sex'] == 'Male']

df[(df['total_bill'] > 40) & (df['sex'] == 'Male')]