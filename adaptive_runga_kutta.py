#solve the differential equation dy/dx=x**2+y**2;y(0)=2,at h=0.1 using adaptive runge-kutta methods.

import numpy as np

# Define the function for dy/dx
def f(x, y):
    return x**2 + y**2

# Initial values
x0 = 0
y0 = 2
h = 0.1  # step size
tol = 1e-4  # tolerance for error

# Adaptive Runge-Kutta method
x = x0
y = y0
while x < 1:
    # Calculate k1, k2, k3, k4
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)

    # Calculate y_new using the fourth-order Runge-Kutta method
    y1 = y + (k1 + 2*k2 + 2*k3 + k4)/6

    # Calculate the error estimate
    error = abs(y1 - y - (k1 + 2*k2 + 2*k3 + k4)/6)

    # Adjust step size if error is too large
    if error > tol:
        h = h/2
    else:
        # Update y and x
        y = y1
        x = x + h

    # Print the results
    print(f"x = {x:.2f}, y = {y:.6f}, h = {h:.4f}")

# Print the final value of y(1)
print(f"y(1) = {y:.6f}")
