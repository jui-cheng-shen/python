#exercise 11 #二分搜尋法
def binary_search(arr,target):
    left,right = 0,len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        return -1

arr = [1,2,3,4,5,6,7,8,9]
print(binary_search(arr,5)) #4(索引值)


#exercise 12 產生指定串列/陣列的所有子集合

def generate_subsets(arr,index=0,subset=[]):
    if index == len(arr):
        print(subset)
        return

    generate_subsets(arr, index+1, subset) #不包含arr[index]
    generate_subsets(arr, index+1, subset+[arr[index]]) #包含arr[index]

arr = [1,2,3]
generate_subsets(arr)