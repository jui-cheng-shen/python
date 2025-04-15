import numpy as np

def CONDITION():
    combination_1 = [1,4]
    combination_2 = [3,1]
    combination_3 = [2,2]
    distance_water = [0,-3,-6]
    return [combination_1, combination_2, combination_3], distance_water

def calulate_length_of_A_B():
    combinations, distances = CONDITION()

    A = []
    B = []

    for i in range(3):
        a, b = combinations[i]
        A.append([a, b, -1]) # -1 的作用是為了讓方程式的右邊等於 0, 即 Ax + By + C = 0
        B.append(distances[i])

    A = np.array(A)
    B = np.array(B)

    result = np.linalg.solve(A, B)
    x, y, d = result

    print("甲家繩子長度：", round(x, 2), "公尺")
    print("乙家繩子長度：", round(y, 2), "公尺")

calulate_length_of_A_B()