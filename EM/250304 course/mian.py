def vecAdd(a,b):
    c = []
    for i in range(len(a)):
        tmp = a[i] + b[i]
        c.append(tmp)
    return c

def innerP(a,b):
    a_b=0
    for i in range(len(a)):
        a_b += a[i]*b[i]
    return a_b

def transP(a):
    at = []
    for i in range(len(a[0])):
        vec =[]
        for j in range(len(a)):
            vec.append(a[j][i])
        at.append(vec)
    return at

def matrixAdd(a,b):
    c = []
    for i in range(len(a)):
        vec = vecAdd(a[i],b[i])
        c.append(vec)
    return c

def matrixP(a,b):
    axb = []
    bt = transP(b)
    for i in range(len(a)):
        vec = []
        for j in range(len(bt)):
            vec.append(innerP(a[i],bt[j]))
        axb.append(vec)
    return axb

a = [1,2]
b = [3,4]
print('a+b+',end='')
print(vecAdd(a,b))  # [4, 6]
print('a dot b=',end='')
print(innerP(a,b))  # 11

a1 = [[1,2],[3,4]]
b1 = [[5,6],[7,8]]
print('a1+b1=',end='')
print(matrixAdd(a1,b1))  # [[6, 8], [10, 12]]

bt1 = transP(b1)
print('b1=',end='')
print(b1)  # [[5, 6], [7, 8]]
print('bt轉置矩陣=',end='')
print(bt1)  # [[5, 7], [6, 8]]

axb = matrixP(a1,b1)
print('a1矩陣乘上b1矩陣=',end='')
print(axb)  # [[19, 22], [43, 50]]