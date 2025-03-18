import numpy as np

A = np.array([[2,4],[1,1]])
B = np.array([[40],[15]])

D = np.array([[1/2,0],[0,1]])

c = np.array([[1,0],[-1,1]])

B_M = np.array([[1,0],[0,-2]])

A_M = np.array([[1,-4],[0,1]])

#1.求ABCD矩陣
ABCD = A_M @ B_M @ c @ D
print("ABCD矩陣:",ABCD)

#2.求 x 的反矩陣
X = np.array([[2,4],[1,1]])
x_inv = np.linalg.inv(X)
print("2. X 的反矩陣:",x_inv)

#3.求 x,y的解
solution = x_inv @ B #solution 作用是求解線性方程組的解
x = solution[0][0]
y = solution[1][0]
print("x,y的解:")
print(f"x={x}",f"y={y}")

