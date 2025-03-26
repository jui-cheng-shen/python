#insertion sort
#21,15,7,33,25,19,11,2
#插入排序透過逐一取出元素，將其插入到已排序區域的適當位置，確保序列保持有序。

arr = [21,15,7,33,25,19,11,2]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print(arr)