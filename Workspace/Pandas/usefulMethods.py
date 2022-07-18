import numpy as np
import pandas as pd

df = pd.read_csv('.\DATA\\tips.csv')

def lastFour(n):
    return str(n)[-4:]
# function

def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'
    # if
# function

df['last_four'] = df['CC Number'].apply(lastFour)
df['yelp'] = df['total_bill'].apply(yelp)

print(df)

def sample(n):
    return n * 2
# function

df['total_bill'].apply(lambda n: n * 2)

def qaulity(totalBill, tip):
    if tip/totalBill > .25:
        return "Generous"
    else:
        return "Other"
    # if
# function

df[['total_bill', 'tip']].apply(lambda df: qaulity(df['total_bill'],df['tip']), axis=1)