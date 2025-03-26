def merge_sort(arr):
    def divide(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            divide(L)
            divide(R)
            merge(arr, L, R)

    def merge(arr, L, R):
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # 處理剩餘的元素
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    divide(arr)  # 這行是關鍵，執行遞歸拆分並合併

if __name__ == '__main__':
    arr = [21, 15, 7, 33, 25, 19, 11, 2]
    merge_sort(arr)
    print(arr)
