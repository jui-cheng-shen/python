# Date: 2021/05/06
# the inverse arr of a 3x3 matrix

import numpy as np

A = np.array([[3, 2, 1],
            [6, 4, 5],
            [5, 7, 3]], dtype=float)


I = np.eye(3)


Aug = np.hstack((A, I))


steps = []

R11 = np.eye(3)
R11[0] /= Aug[0, 0]
Aug[0] /= Aug[0, 0]
steps.append(R11)


R12 = np.eye(3)
R12[1, 0] = -Aug[1, 0]
R12[2, 0] = -Aug[2, 0]
Aug[1] -= Aug[1, 0] * Aug[0]
Aug[2] -= Aug[2, 0] * Aug[0]
steps.append(R12)


R22 = np.eye(3)
R22[1] /= Aug[1, 1]
Aug[1] /= Aug[1, 1]
steps.append(R22)


R23 = np.eye(3)
R23[0, 1] = -Aug[0, 1]
R23[2, 1] = -Aug[2, 1]
Aug[0] -= Aug[0, 1] * Aug[1]
Aug[2] -= Aug[2, 1] * Aug[1]
steps.append(R23)

R33 = np.eye(3)
R33[2] /= Aug[2, 2]
Aug[2] /= Aug[2, 2]
steps.append(R33)


R34 = np.eye(3)
R34[0, 2] = -Aug[0, 2]
R34[1, 2] = -Aug[1, 2]
Aug[0] -= Aug[0, 2] * Aug[2]
Aug[1] -= Aug[1, 2] * Aug[2]
steps.append(R34)

A_inv = Aug[:, 3:]


R_total = R34 @ R33 @ R23 @ R22 @ R12 @ R11


print("A 的反矩陣:")
print(A_inv)
print("計算的 R 矩陣乘積:")
print(R_total)
print("是否相等:", np.allclose(A_inv, R_total))
