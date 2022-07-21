import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,50)
y = 2 * x
plt.plot(x,y)
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.title('CHART TITLE')
plt.show()