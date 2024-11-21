import random
data=[1,5,6,7,10,20];
random.shuffle(data);
print(data);
#隨機取得亂數
data=random.random();#取得0~1之間的亂數
print(data);
#取得1~30之間的亂數
data=random.uniform(1,30);
print(data);
#取得1~30之間的亂數
data-random.randint(1,30);
print(data);
