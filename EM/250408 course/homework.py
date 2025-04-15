import numpy as np

A = np.array([[1, -2, 1, -1],
                [2, -3, 4, -3],
                [2, -5, 5, -1],
                [-1, 2, -3, 2]])


b = np.array([-4, -4, 3, 3])

x = np.linalg.solve(A, b)


print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])
print("x4 =", x[3])