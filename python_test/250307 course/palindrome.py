#palindrome
#5b1g0012 沈睿晟

import tkinter as tk  # 匯入 Tkinter 用於建立圖形化使用者介面

def palindrome(n):
    n_str = str(n)  # 將輸入轉為字串，以處理數字等情況
    length = len(n_str)
    half = length // 2

    if n_str[:half] == n_str[-half:][::-1]:
        result = f"{n_str} 是一個回文"
    else:
        result = f"{n_str} 不是回文"
    print(result)
    return result


def main():
    win = tk.Tk()
    win.geometry('800x400')  # 設定視窗大小
    win.title('回文判斷')

    group = tk.LabelFrame(win, text='應檢人資料')
    group.pack(padx=10, pady=10)  #padding

    bdata = [
        ["姓名", "王小美", "術科測試編號", "11101123"],
        ["座號", "60", "考試日期", "2024-08-15"]
    ]

    # 在標籤框架中以表格形式顯示資料
    for i in range(2):
        for j in range(4):
            tk.Label(group, text=bdata[i][j]).grid(row=i, column=j, padx=5, pady=5)


    tk.Label(win, text="請輸入字串以檢查是否為回文：").pack(pady=5)
    entry = tk.Entry(win)  # 文字輸入框
    entry.pack(pady=5)

    # 顯示結果的標籤
    result_label = tk.Label(win, text="")
    result_label.pack(pady=5)

    # 檢查按鈕的功能
    def check_palindrome():
        user_input = entry.get()  # 獲取輸入框的文字
        result = palindrome(user_input)  # 呼叫回文判斷函數
        result_label.config(text=result)  # 更新結果標籤

    tk.Button(win, text="檢查", command=check_palindrome).pack(pady=5)  # 檢查按鈕

    win.mainloop()  # 啟動 GUI 事件循環

if __name__ == "__main__":
    main()