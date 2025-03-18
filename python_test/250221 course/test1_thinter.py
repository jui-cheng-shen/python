import tkinter as tk #thinder 為圖形化介面的模組

root = tk.Tk()

frame = tk.Frame(root) #設定一個框架
frame.pack()

label = tk.Label(root, text="Hello, World!")

button = tk.Button(root, text="cllick me!")

entry = tk.Entry(root) #輸入框

listbox = tk.Listbox(root) #列表框
listbox.insert(tk.END, "apple" ,"banana", "orange") #tk.END 為插入的位置

label.pack()
button.pack()
entry.pack()
listbox.pack()

root.mainloop()

