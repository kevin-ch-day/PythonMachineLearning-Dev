import pandas as pd
import os

print(os.getcwd)
df = pd.read_csv('.\DATA\\example.csv')
print(df)


df.to_csv('.\OUTPUT\\exampleOutput.csv')