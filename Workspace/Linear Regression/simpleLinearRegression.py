import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Advertising.csv")
#print(df.head())

df['total_spend'] = df['TV'] + df['radio'] + df['newspaper']
#print(df.head())

#sns.scatterplot(data=df, x='total_spend', y='sales')
sns.regplot(data=df, x='total_spend', y='sales')
#plt.show()

feature = df['total_spend']
target = df['sales']

# y= mx+b
# y = b1x+b0

result = np.polyfit(feature, target, deg=1)
#print(result)

potential_spend = np.linspace(0, 500, 100)
predicted_sales = result[0] * potential_spend + result[1]
#print(predicted_sales)

#sns.scatterplot(data=df, x='total_spend', y='sales')
#plt.plot(potential_spend, predicted_sales, color='red')
#plt.show()

spend = 200
predicted_sales = result[0] * potential_spend + result[1]
#print(predicted_sales)

# y = b3^3 + b2x^2 + b1x + b0
result = np.polyfit(feature, target, deg=3)
potential_spend = np.linspace(0, 500, 100)
predicted_sales = result[0] * potential_spend ** 3 # B3^3
predicted_sales = predicted_sales + result[1] * potential_spend ** 2 # B2x^2
predicted_sales = predicted_sales + result[2] * potential_spend # b1x
predicted_sales = predicted_sales + result[3] # b0

sns.scatterplot(data=df, x='total_spend', y='sales')
plt.plot(potential_spend, predicted_sales, color='red')
plt.show()