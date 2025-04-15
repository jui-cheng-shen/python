def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(M, name="Matrix"):
    print(f"{name}:")
    for row in M:
        print(" ", row)
    print()


A = [
    [1, 2, 3],
    [2, 5, 7],
    [3, 5, 3]
]


L2 = [
    [1, 0, 0],
    [-2, 1, 0],
    [-3, 0, 1]
]


L1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 1]
]

L2A = matrix_multiply(L2, A)
print_matrix(L2A, "L2 * A")


L1_L2A = matrix_multiply(L1, L2A)
print_matrix(L1_L2A, "L1 * L2 * A")
