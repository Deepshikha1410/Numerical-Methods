#The trapezoidal Rule for given function
import numpy as np
import scipy.integrate._quadpack as quadpack 
def IT(f,a,b,n):
    h =(b-1)/n
    sum =0
    for i in range(int(n)):
        t = (f(a+i*h) + f(a+(i+1)*h))
        sum = sum+t
    return sum*h/2
def f(x):
    y=2+2*x+x**2+np.sin(2*np.pi*x)+np.cos(2*np.pi*x/0.5)
    return y
print(IT(f,0,1.5,1.0))
print(IT(f,0,1.5,9.0))