import numpy as np

def CONDITION():
    every_day_sell = 100
    today_sell_income = 531
    today_guest = 50
    price_array = [6, 11, 15]
    return every_day_sell, today_sell_income, today_guest, price_array

def calculate():
    every_day_sell, today_sell_income, today_guest, price_array = CONDITION()

    for x in range(today_guest + 1):
        for y in range(today_guest - x + 1):
            z = today_guest - x - y
            total_sell = x * 1 + y * 2 + z * 3
            total_income = x * price_array[0] + y * price_array[1] + z * price_array[2]
            if total_sell == every_day_sell and total_income == today_sell_income:
                print("買 1 個饅頭的人數:", x)
                print("買 2 個饅頭的人數:", y)
                print("買 3 個饅頭的人數:", z)
                return

calculate()
