lst=[22,33,12,66,55]
for j in range(len(lst)-1):
    if lst[j]>lst[j+1]:
        lst[j],lst[j+1]=lst[j+1],lst[j]
for x in lst:
    print('%3d' % (x),end=' ')