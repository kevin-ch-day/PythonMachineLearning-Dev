import numpy as np
import pandas as pd

df = pd.read_csv('.\DATA\\movie_scores.csv')

print(df[df['pre_movie_score'].notnull()])

print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])

df.dropna(thresh=1)

df.dropna(axis=0)

df.dropna(subset=['last_name'])

df['pre_movie_score'].fillna(0)
df['pre_movie_score'].mean()
df.fillna(df.mean())