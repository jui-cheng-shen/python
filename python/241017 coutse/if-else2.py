x = int(input("身上有多少錢"))
if x >= 100:
    print("吃蛋糕")
else:
    eat = input("吃過布丁了嗎?").lower() == 'true' #lower()轉小寫
    if eat:
        print("吃布丁")
    else:
        print("喝優酪乳")