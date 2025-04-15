import numpy as np

x, y = 1, 2


cos_theta = 4 / 5
sin_theta = 3 / 5

rotation_matrix = np.array([
    [cos_theta, sin_theta],
    [-sin_theta, cos_theta]
])

rotated_point = rotation_matrix @ np.array([x, y])


x_prime = int(rotated_point[0])
y_prime = int(rotated_point[1])


print(f"旋轉後的座標：[{x_prime:.6f}, {y_prime:.6f}]")