import numpy as np
import pandas as pd

# part one
countryNames = ["USA", "CANADA", "MEXICO"]
startingYears = [1776, 1868, 1821]
x = pd.Series(data=startingYears, index=countryNames)
print(x)
print() # newline

ages = {'Sam':5, "Frank":10, "Sally":7}
y = pd.Series(ages)
print(y)

expenses = pd.Series({'Andrew':200,'Bob':150,'Claire':450})
bob_expense = expenses['Bob']

# part two
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}

salesQ1 = pd.Series(q1)
salesQ2 = pd.Series(q2)
print(salesQ1, "\n", salesQ2, "\n")

print(salesQ1['Japan'])
print(salesQ1.keys())

print(salesQ1 * 2)

print(salesQ1.add(salesQ2, fill_values = 0))