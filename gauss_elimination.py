#Solve any 3 linear equation of your choice using Gauss Elimination method.
import numpy as np

def gauss_elimination(A, b):
    n = len(A)
    # Forward elimination
    for i in range(n):
        # Find the pivot element
        pivot = A[i][i]
        # Divide the row by the pivot element
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot
        # Eliminate the elements below the pivot
        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
    # Backward substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
    return x

# Example usage
A = np.array([[2, 1, 1], [3, 2, 1], [1, 1, 2]])
b = np.array([8, 14, 9])

x = gauss_elimination(A, b)

print("Solution:", x)