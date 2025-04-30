#費式數列
#example: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

n = [int(x) for x in input("請輸入費式數列的項數: ").split()]
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

