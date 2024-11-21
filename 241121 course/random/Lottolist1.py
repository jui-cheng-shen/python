import random;
lotto = [];#建立一個空的list
count = 1;
while count <= 6:
    num = random.randint(1, 49);
    if num not in lotto: #如果num不在lotto裡面
        lotto.append(num);#將num加入到lotto裡面
        count += 1;
        print(lotto);