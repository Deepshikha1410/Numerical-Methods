#Write a python code for Trapezoidal Rule to calculate integration ∫(𝑥=0 to 1.5) 𝑓(𝑥)𝑑𝑥 if 𝑓(𝑥)=2+2𝑥+𝑥^2+sin⁡(2𝜋𝑥)+cos⁡(2𝜋𝑥/0.5)
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 2 + 2*x + x**2 + np.sin(2*np.pi*x) + np.cos(2*np.pi*x/0.5)
    return y

x = np.linspace(0, 1.5, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x)')
plt.grid(True)
plt.show()