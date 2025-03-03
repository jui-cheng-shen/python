#exercise 1 印出hello world
print("Hello world!")

#exercise 2-1 印出指定次數的hello world
n = 8
for i in range(1, n+1):
    print("hello world")

#exercise 2-2 印出指定次數一半的hello world
n = 8
for i in range(1, n+1 ,2):
    print("hello world")


#exercise 3 印出指定次數的hello world
n = 8
i = 1
while i <= n:
    print("hello world")
    i *= 2

#exercise 4 印出指定次數規則變化的hello world
n = 8
i = 1
for i in range(2, n+1):
    if i >= n :
        break;
    else:
        print("hello world")
    i *= i;

#exercise 5 計算兩數相加
a = 5
b = 6

def sum(a,b):
    return a + b

print(sum(a,b))



