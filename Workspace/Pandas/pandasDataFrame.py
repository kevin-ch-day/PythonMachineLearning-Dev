import numpy as np
import pandas as pd

#np.random.seed(9999)

states = ['CA', 'NY', 'AZ', 'TX', 'MN', 'WI', 'SD', 'ND']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

x = np.random.randint(0, 99999, (len(states), len(months)))

df = pd.DataFrame(data=x, index=states, columns=months)
print(df)
#print(df.info)

df_csv = pd.read_csv('.\DATA\\tips.csv')
print(df_csv)