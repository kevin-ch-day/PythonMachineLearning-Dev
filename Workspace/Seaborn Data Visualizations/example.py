#scatterplots

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dm_office_sales.csv')
#print(df.head())

plt.figure(figsize=(12,4))
sns.scatterplot(x='salary',y='sales',data=df,style='level of education',hue='level of education')
plt.show()