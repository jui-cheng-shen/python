x, y=input("Enter a number:").split()
num1=int(x)
num2=int(y)
while num1 < num2:
    for i in range(num1,num2):
        num1 += i;
    print(num1)

