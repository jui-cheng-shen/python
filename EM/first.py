a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
am=len(a)
an=len(a[0])
bm=len(b)
bn=len(b[0])
print(f'a的列數={am},a的行數={an}')
print(f'b的列數={bm},b的行數={bn}')


puls=[]
for i in range(am):
    vec=[]
    for r in range(an):
        el= a[i][r]+b[i][r]
        vec.append(el)
    puls.append(vec)

print('a+b=',end=' ')
print(puls)