import math


A = [1, 2, 3]
B = [4, 5, 6]


dot_product = sum(a * b for a, b in zip(A, B))

magnitude_A = math.sqrt(sum(a ** 2 for a in A))
magnitude_B = math.sqrt(sum(b ** 2 for b in B))


cos_theta = dot_product / (magnitude_A * magnitude_B)

theta_radians = math.acos(cos_theta)


theta_degrees = math.degrees(theta_radians)


print(f"向量 A 和 B 的夾角 (度): {theta_degrees:.4f}")