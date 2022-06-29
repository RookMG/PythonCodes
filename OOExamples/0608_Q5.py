from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-2,8,0.01)
y = -x**2 + 5*x + 1

plt.plot(x,y,marker='',linestyle='--',color='r')

plt.grid()
plt.show()