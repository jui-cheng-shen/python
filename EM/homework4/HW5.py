import numpy as np

def CONDITION():
    combination_1 = [10, 10, 10]
    combination_2 = [0, 15, 15]
    combination_3 = [15, 0, 30]
    total_output = [30000, 30000, 30000]
    return [combination_1, combination_2, combination_3], total_output

def calculate_production_hours_of_Y_only():
    A, B = CONDITION()

    A = np.array(A)
    B = np.array(B)

    result = np.linalg.solve(A, B)
    x, y, z = result

    hours_for_y = 30000 / y
    print("需要", round(hours_for_y, 2), "小時")

calculate_production_hours_of_Y_only()
