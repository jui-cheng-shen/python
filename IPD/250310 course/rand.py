import random

target_number = random.randint(1, 100)
guess_history = []
max_attempts = 7

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"第 {attempt} 次猜測，請輸入數字："))
    # 存入猜測歷史
    guess_history.append(guess)
    if guess == target_number:
        print(f"恭喜！你在第 {attempt} 次猜中了！答案是 {target_number} 🎯")
        break
    elif guess < target_number:
        print("太小了！")
    else:
        print("太大了！")
    print(f"你的猜測歷史：{guess_history}")
else:
    print(f"遊戲結束，你沒能猜中。正確答案是 {target_number}！")
