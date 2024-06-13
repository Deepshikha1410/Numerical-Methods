#using modified euler's method to obtain y(0.2) correct to 3 decimal place,given that dy/dx=y-x**2;y(0)=1  

import numpy as np

# Define the function for dy/dx
def f(x, y):
    return y - x**2

# Initial values
x0 = 0
y0 = 1
h = 0.1  # step size

# Calculate y(0.2) using Modified Euler's method
x = x0
y = y0
for _ in range(2):  # iterate twice to reach x = 0.2
    yp = f(x, y)
    y_new = y + h * yp + h/2 * f(x + h, y + h * yp)
    x = x + h
    y = y_new

# Print the result to 3 decimal places
print(f"y(0.2) = {y:.3f}")
