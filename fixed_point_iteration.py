#Write a python program to find a root of a equation 𝑓(𝑥) = 𝑐𝑜𝑠𝑥 − 𝑥 using fixed point method. Assume error tolerance is 0.001.
from math import cos
def f(x):
    return cos(x)-x

def fixed_point_iteration(x, tol,n):
    for i in range(n):
        f= cos(x)
        error = abs(x - f)
        print(f"Iteration {i+1}: f = {f},error ={error}")
        if error < tol:
            return f
        x = f
    return None

x = 0.1  # Initial guess
tol = 1e-3  # Tolerance
n = 25  #number of iterations

root = fixed_point_iteration(x, tol, n)

if root is not None:
    print("The root of the equation is:", root)
else:
    print("The root could not be found within the specified tolerance and  iterations.")