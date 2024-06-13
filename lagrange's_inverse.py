#write a program in python for lagrange's interpoltation for y = 4.5
import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = np.array([1, 2, 3, 4])
y = np.array([1.1, 2.1, 5, 7])

# Value of y for which we want to find x
y_val = 4.5

# Calculate Lagrange interpolating polynomial
def lagrange_interpolation(x, y, y_val):
    n = len(x)
    p = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (y_val - y[j]) / (y[i] - y[j])
        p += x[i] * l
    return p

# Find x for y = 4.5
x_val = lagrange_interpolation(x, y, y_val)

# Print the result
print(f"x value for y = {y_val} is: {x_val}")

# Plot the data points and the interpolating polynomial
plt.plot(x, y, 'o', label='Data Points')
x_interp = np.linspace(x[0], x[-1], 100)
y_interp = lagrange_interpolation(x, y, x_interp)
plt.plot(x_interp, y_interp, label='Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()