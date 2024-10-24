n=0
for x in [0,1,2,3]:
    if x%2==0:
        continue #continue 語句會跳過當前迴圈的剩餘代碼，直接進入下一次迴圈的迭代。
    print("x=",x,end=" ")
    n=n+1
print(n)