import numpy as np

def CONDITION():
    combination_1 = [1,3,2]
    combination_2 = [2,1,3]
    combination_3 = [3,2,1]
    price = [215, 215, 200]
    A = np.array([combination_1, combination_2, combination_3])
    B = np.array(price)
    return A, B

def calculate():
    A, B = CONDITION()
    result = np.linalg.solve(A, B)
    result = np.round(result, 2)
    print("低筋麵粉 每斤價格:", result[0], "元")
    print("中筋麵粉 每斤價格:", result[1], "元")
    print("高筋麵粉 每斤價格:", result[2], "元")

calculate()