import numpy as np

def CONDITION():
    sell_everyday = 999
    today_sell_income = 7195
    today_guest =  435
    manny_1 = 8
    manny_2 = 16
    manny_3 = 21

    A = np.array([
        [1, 1, 1],
        [1, 2, 3],
        [manny_1, manny_2, manny_3]
    ])

    B = np.array([
        today_guest,
        sell_everyday,
        today_sell_income
    ])

    result = np.linalg.solve(A, B)

    one_bao = int(result[0])
    two_bao = int(result[1])
    three_bao = int(result[2])

    print(f"買 1 個包子的人數：{one_bao} 人")
    print(f"買 2 個包子的人數：{two_bao} 人")
    print(f"買 3 個包子的人數：{three_bao} 人")

    profit = one_bao * manny_1 + two_bao * manny_2 + three_bao * manny_3
    print(f"當天白羅包子店淨賺：{profit} 分")

CONDITION()
