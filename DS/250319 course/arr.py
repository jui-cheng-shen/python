arr = [2,6,9,11,8]
n = len(arr)


for i in range(1,n,1):
    if i == n-1:
        print(arr[i])
    else:
        print(arr[i],end="---")

for i in range(n-1,-1,-1):
    if i == 0:
        print(arr[i])
    else:
        print(arr[i],end="---")

