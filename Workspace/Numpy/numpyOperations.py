import numpy as np

a = np.arange(0, 5)

print(a + 5)
print(a - a)
print(a * 5)

print(a / a) # RuntimeWarning 0/0
print(1 / a) # RuntimeWarning 1/0

print(np.sqrt(a))
print(np.sin(a))
print(np.log(a))