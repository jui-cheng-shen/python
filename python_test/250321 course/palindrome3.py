#palindrome
#5b1g0012
import tkinter as tk

def page():
    global win, group #global宣告全域變數
    win = tk.Tk()
    win.geometry("800x400")
    win.title('求出分數的加、減、乘、除運算')

    group = tk.LabelFrame(win, text='應檢人資料')
    group.pack(padx=10, pady=10)

def DATA():
    global bdata
    bdata = [
    ['姓名', '王小美', '術科測試編號', '11101123'],
    ['座號', '99', '考試日期', '2025-03-21']
]

def show():
    rowN = 0
    while rowN < 2:
        columnN = 0
        while True:
            t= tk.Label(group, text=bdata[rowN][columnN])
            t.grid(row=rowN, column=columnN)
            columnN += 1
            if columnN >= 4:
                break
            else:
                continue
        rowN += 1

def Openfile():
    global data
    with open(r'D:\test\1060301.SM', 'r') as f: #r''是原始字串
        #原始字串不會對反斜線進行轉義，所以字符串內的每個反斜線都需要轉義
        data = f.readline().strip() #strip() 方法用於移除字符串頭尾指定的字符（默認為空格或換行符）或字符序列
    return data

def judgeMath():
    global resultLabel
    result=''
    n=int(data)
    c,i=0,1

    while i<=n:
        if n%i==0:
            c+=1
        i+=1

    if c==2:
        result=f'第三題結果:{data} is a prime number'
    else:
        result=f'第三題結果:{data} is not a prime number'

    resultLabel = tk.Label(win, text=result, font=("Arial", 12))
    resultLabel.pack(pady=20)

if __name__ == '__main__':
    page()
    DATA()
    show()
    Openfile()
    judgeMath()
    win.mainloop()