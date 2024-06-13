#Using Gauss Quadrature method solve f(x)=Sin(x)+Cos(x) on the interval [-1,1]
import numpy as np
from scipy.special import legendre
from scipy.integrate import quad

def f(x):
    return np.sin(x) + np.cos(x)

# Gauss-Legendre quadrature with n=2
n = 2
x, w = np.polynomial.legendre.leggauss(n)
result = 0
for i in range(n):
    result += w[i] * f(x[i])

print("Gauss-Legendre quadrature result:", result)

# Compare with scipy.integrate.quad
result_quad = quad(f, -1, 1)[0]
print("quad result:", result_quad)