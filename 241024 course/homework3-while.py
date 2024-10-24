import random;
Q = random.randint(1, 20);
G=int (input("輸入一個數字:"));
while G != Q:
    print("再試一次");
    if G > Q:
        print("數字太大了");
    else:
        print("數字太小了");
    G=int(input("輸入一個數字:"));
print("你猜對了");
