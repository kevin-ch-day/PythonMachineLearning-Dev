import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,10,11)
b = a ** 4

x = np.arange(0,10)
y = 2 * x

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y)
plt.show()