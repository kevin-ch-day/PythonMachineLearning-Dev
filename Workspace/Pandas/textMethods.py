import numpy as np
import pandas as pd

email = 'First.Last@gmail.com'
print(email.split('@'))

names = pd.Series(['Andrew', 'BoBo', 'Sam', 'David', '5'])
print(names.str.upper())
print(names.str.isdigit())

from datetime import datetime

y = 1999
m = 1
d = 2
hr = 2
min = 30
sec = 15

aDate = datetime(y, m, d, hr, min, sec)
print(aDate)