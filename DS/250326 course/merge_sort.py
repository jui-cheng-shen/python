#merge_sort
#21,15,7,33,25,19,11,2
#合併排序透過遞迴將數列拆分成最小單位，然後依序合併已排序的部分，最終形成完整的排序結果。 🚀

'''
for example:
DIVIDE:[21,15,7,33,25,19,11,2] -> [21,15,7,33] [25,19,11,2] -> [21,15] [7,33] [25,19] [11,2] -> [21] [15] [7] [33] [25] [19] [11] [2]
MERGE:-> [15,21] [7,33] [19,25] [2,11] -> [7,15,21,33] [2,11,19,25] -> [2,7,11,15,19,21,25,33]
'''

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [21,15,7,33,25,19,11,2]
    merge_sort(arr)
    print(arr)