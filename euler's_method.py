#write a program in python using euler's method.compute y(0.12) for initial value problems: dy/dx = x^3 + y; y(0)=1,taking h=0.02 

import numpy as np
def f(x,y):
    return x**3 + y
x0 = 0
y0 = 1
h = 0.02
n = 6
x = np.zeros(n+1)
y = np.zeros(n+1)
x[0] = x0
y[0] = y0
for i in range(n):
    x[i+1] = x[i] + h
    y[i+1] = y[i] + h*f(x[i],y[i])
print("y(0.12) = ",y[6])
print(y)

