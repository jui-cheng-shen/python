import random
from flask import Flask

app = Flask(__name__)

r = random.randint(1, 100)

@app.route("/<msg>")
def ok(msg):
    global r
    try:
        guess = int(msg)
        if guess == r:
            return f'YES you hit the {r}'
        else:
            return f'錯了！r 是 {r}，你猜的是 {guess}'
    except ValueError:
        return '請輸入一個有效的數字！'

if __name__ == '__main__':
    print(f"程式啟動，隨機數 r = {r}")  # 顯示初始 r
    app.run(host='0.0.0.0', port=5000, debug=True)  # 改用 5000 埠