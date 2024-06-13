#Solve any 3 linear equation of your choice using Gauss Elimination method.
import numpy as np

# Define the coefficient matrix A and the right-hand side vector b
A = np.array([[2, 1, 1], [4, 3, 1], [1, 2, 3]])
b = np.array([7, 13, 11])

# Perform Gauss Elimination
n = len(A)
for i in range(n):
    # Search for maximum in this column
    max_el = abs(A[i, i])
    max_row = i
    for k in range(i+1, n):
        if abs(A[k, i]) > max_el:
            max_el = abs(A[k, i])
            max_row = k

    # Swap maximum row with current row
    A[[i, max_row]] = A[[max_row, i]]
    b[[i, max_row]] = b[[max_row, i]]

    # Make all rows below this one 0 in current column
    for k in range(i+1, n):
        c = -A[k, i]/A[i, i]
        for j in range(i, n):
            A[k, j] += c * A[i, j]
        b[k] += c * b[i]

# Back-substitution
x = np.zeros(n)
x[n-1] = b[n-1] / A[n-1, n-1]
for i in range(n-2, -1, -1):
    x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

print("Solution:", x)