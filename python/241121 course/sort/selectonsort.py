def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap 是 Python 中用來交換兩個變數的語法
        nums[i], nums[min_index] = nums[min_index], nums[i]

unms = [5,4,3,1,2]
print("before sort %s"% unms)
selection_sort(unms)
print("after sort %s"% unms)