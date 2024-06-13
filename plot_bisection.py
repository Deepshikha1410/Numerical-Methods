import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin

def fun(x):
    z = np.sin(x*5) + np.cos(x*2)
    return z

def bisection(a,b):
    print("Checking for a=",a,"b=",b)
    for i in range(0,35):
        if fun(a)*fun(b) < 0 :
            xi=(a+b)/2
            if round(fun(xi),4)==0:
                print("Roots of given equation is ",xi)
                break
            elif (fun(xi)*fun(a))<0:
                print("Shifting value of b")
                b=xi
            elif (fun(xi)*fun(b))<0:
                print("Shifting value of b")
                a=xi
        else:
            print("Roots does not exist between a=",a,"b=",b)
            break

# Function call
bisection(-0.6,-0.5)
bisection(-0.3,-0.2)
bisection(0.1,0.9)

# Plot the graph
x = np.linspace(-1, 1, 400)
y = fun(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of the function')
plt.grid(True)
plt.axhline(0, color='black')
plt.show()