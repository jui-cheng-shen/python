#exercise 6 計算串列中所有元素的總和

def list_sum(A,n):
    sum = 0
    for i in range(n):
        sum += A[i]
    return sum
A = [5,6,1,2]
n = len(A)
print(list_sum(A,n))

#exercise 7 計算矩陣中所有元素的總和

n = 3
m = 3
arr = [[3, 2, 7], [2, 6, 8], [5, 1, 9]]
sum = 0
for i in range(n):
    for j in range(m):
        sum += arr[i][j]
print(sum)

#exercise 8 找出陣列中的最大值
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(find_max(arr))

#exercise 9 氣泡排序法
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr = [5, 3, 8, 4, 2]
print(bubble_sort(arr))

#exercise 10 合併排序法
def mearg_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #找出arr的中間位置
    left_half=mearg_sort(arr[:mid]) #將arr分成左右兩邊
    right_half=mearg_sort(arr[mid:]) #將arr分成左右兩邊

    return merge(left_half, right_half) #合併左右兩邊的元素

def merge(left,right):
    sorted_arr = []
    i=j=0;

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1;
        else:
            sorted_arr.append(right[j])
            j += 1;

    sorted_arr.exxtend(left[i:]) #若左邊有剩餘元素,則將左邊剩餘元素加入sorted_arr
    sorted_arr.exxtend(right[j:]) #若右邊有剩餘元素,則將右邊剩餘元素加入sorted_arr
    return sorted_arr

arr = [5, 3, 8, 4, 2, 7, 1, 6]
sorted_arr = mearg_sort(arr)
print(sorted_arr) #output: [1, 2, 3, 4, 5, 6, 7, 8]

#output:
# 14
# 9
# 9
# [2, 3, 4, 5, 8]
# [1, 2, 3, 4, 5, 6, 7, 8]
#
# The output of the code is:
# 14
# 9
# 9
