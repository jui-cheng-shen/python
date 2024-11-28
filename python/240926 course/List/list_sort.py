a = [0, 3, 6, 1, 4, 9, 8, 7, 5]  # 定義一個包含九個整數的列表 a
b = sorted(a)  # 使用 sorted 函數對列表 a 進行升序排序，並將結果賦值給變數 b
c = sorted(a, reverse=True)  # 使用 sorted 函數對列表 a 進行降序排序，並將結果賦值給變數 c

print(a)  # 輸出原始列表 a，應該是 [0, 3, 6, 1, 4, 9, 8, 7, 5]
print(b)  # 輸出升序排序後的列表 b，應該是 [0, 1, 3, 4, 5, 6, 7, 8, 9]
print(c)  # 輸出降序排序後的列表 c，應該是 [9, 8, 7, 6, 5, 4, 3, 1, 0]