import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gene_expression.csv')
#print(df.head())
numPoints = len(df)

sns.scatterplot(data=df,x='Gene One',y='Gene Two',hue='Cancer Present',alpha=0.6,style='Cancer Present')
sns.pairplot(data=df,hue='Cancer Present')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x = df.drop('Cancer Present',axis=1)
y = df['Cancer Present']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(x_train)
scaled_X_test = scaler.transform(x_test)