#偶數長度陣列: 將後半部分和前半部分互換
#奇數長度陣列: 保留中間元素，將前半部分和後半部分互換
#定義函式 fold(arr)，將輸入的陣列 arr 依照上述規則進行處理，並回傳處理後的陣列。

def fold(arr):
    n = len(arr)
    half = n // 2

    if n % 2 == 0:
        arr[:half], arr[half:] = arr[half:], arr[:half]
    else:
        arr[:half], arr[half+1:] = arr[half+1:], arr[:half]
        #half+1: 意思是從half+1開始到最後一個元素,for example: half=3, arr[4:] = arr[4], arr[5], arr[6], arr[7], arr[8], arr[9]
    return arr

a1 = [1, 3, 5, 7, 11, 22, 33]
a2 = [1, 3, 5, 11, 22, 33]

print(fold(a1))
print(fold(a2))
