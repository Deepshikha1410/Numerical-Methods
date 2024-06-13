import numpy as np
import matplotlib.pyplot as plt
M = [(1,1,1,1),[1,2,2**2,2**3],[1,3,3**2,3**3],[1,3.4,3.4**2,3.4**3]]
yv = [1.1,2.1,5,7]
a = np.matmul(np.linalg.inv(M),yv)
x_val = np.arange(0,4,0.01)
y_val = []
for i in x_val:
    y_val.append(a[0]+a[1]*i+a[2]*i**2+a[3]*i**3)
plt.plot(x_val,y_val)
plt.scatter([1,2,3,3.4],[1.1,2.1,5,7], c='k')
plt.grid();plt.show()