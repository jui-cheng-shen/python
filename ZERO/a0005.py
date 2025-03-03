#等差or等比
def find_fifth_term(sequence):
    # 假設 sequence 是包含前四項的列表
    a1, a2, a3, a4 = sequence

    # 判斷是否為等差數列
    if (a2 - a1) == (a3 - a2) == (a4 - a3):
        # 等差數列的公差
        d = a2 - a1
        # 計算第五項
        a5 = a4 + d
        print(f"這是等差數列，第五項是: {a5}")

    # 判斷是否為等比數列
    elif (a2 / a1) == (a3 / a2) == (a4 / a3):
        # 等比數列的公比
        r = a2 / a1
        # 計算第五項
        a5 = a4 * r
        print(f"這是等比數列，第五項是: {a5}")

    else:
        print("這個數列既不是等差數列也不是等比數列。")

# 測試範例
sequence = [2, 4, 6, 8]  # 等差數列
find_fifth_term(sequence)

sequence = [3, 6, 12, 24]  # 等比數列
find_fifth_term(sequence)

sequence = [1, 2, 4, 8]  # 這不是等差也不是等比數列
find_fifth_term(sequence)
