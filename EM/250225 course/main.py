a = [1,2]
b = [3,4]
c=[]

for i in range(len(a)):
    tmp=a[i]+b[i] # tmp=1+3, tmp=2+4
    c.append(tmp) # c=[4,6]

print('a+b=0,', end=' ')
print(c)

al=[[1,2],[3,4]]
bl=[[5,6],[7,8]]
cl=[]

for i in range(len(al)):
    vec=[]
    for j in range(len(al[i])):
        tmp=al[i][j]+bl[i][j] # tmp=1+5, tmp=2+6
        vec.append(tmp) # vec=[6,8]
    cl.append(vec) # cl=[[6,8],[10,12]]

print('al+bl=', end=' ')
print(cl) # [[6,8],[10,12]]