def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(num, denom):
    if denom == 0:
        raise ValueError("分母不能為 0")
    if num == 0:
        return 0, 1
    g = gcd(num, denom)
    return num // g, denom // g


def print_matrix(matrix, name):
    print(f"{name}:")
    for row in matrix:
        row_str = []
        for val in row:
            if isinstance(val, tuple):
                num, denom = val
                if denom == 1:
                    row_str.append(str(num))
                else:
                    row_str.append(f"{num}/{denom}")
            else:
                row_str.append(str(val))
        print("[" + " ".join(row_str) + "]")
    print()

def inverse_matrix(A):
    n = len(A)

    augmented = []
    for i in range(n):
        row = A[i].copy()
        for j in range(n):
            row.append(1 if i == j else 0)
        augmented.append(row)

    for i in range(n):
        pivot = augmented[i][i]
        if pivot == 0:
            raise ValueError("不可逆")

        for j in range(2 * n):
            augmented[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]

    inverse = []
    for i in range(n):
        row = []
        for j in range(n, 2 * n):
            num = round(augmented[i][j] * 1000000)
            denom = 1000000
            num, denom = simplify_fraction(num, denom)
            row.append((num, denom))
        inverse.append(row)

    return inverse

A = [
    [1, 1, 1, 0],
    [0, 3, 1, 2],
    [2, 3, 1, 0],
    [1, 0, 2, 1]
]


A_inverse = inverse_matrix(A)


print_matrix(A_inverse, "A 的反矩陣 A^-1")