import numpy as np

# test 1
a = np.arange(0, 11)
a[0:5] = 100
print(a)

b = a[0:5] # reference
print(b)

b[:] = 52
print(b)
print(a)

c = a.copy() # copy
c[:] = 99
print(c)
print(a)

# test 2
d  = np.array([[1,2,3],[4,5,6],[4,5,6]])
print("Shape: ", d.shape)
print(d[1,1]) # print(d[1][1])