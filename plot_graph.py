#𝑓 𝑥 = −𝑥 2 + 4𝑥 + 5
# 𝑓 ′ 𝑥 = −2𝑥 + 4
# 𝑓 ′′ 𝑥 = −2
# 𝑓 0.3 = −0.3 2 + 4 ∗ 0.3 + 5 =6.109
# 𝑓′ 0.3 = −2 ∗ 0.3 + 4 = 3.4
# 𝑓 ′′ 0.3 = −2
# Assignment: Plot a f(x), f’(x),f’’(x) for a different values of -2<x<6

import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return -x**2 + 4*x + 5

def df(x):
    return -2*x + 4

def ddf(x):
    return -2

# Generate x values
x = np.linspace(-2, 6, 100)

# Calculate y values for each function
y_f = f(x)
y_df = df(x)
y_ddf = ddf(x)

# Plot the graphs
plt.plot(x, y_f, label='f(x)')
plt.plot(x, y_df, label='f\'(x)')
plt.plot(x, y_ddf, label='f\'\'(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of f(x), f\'(x), and f\'\'(x)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()