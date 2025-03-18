import tkinter as tk
win=tk.Tk()
win.geometry("800x400")
win.title('求出分數的加,減,乘,除運算')
group=tk.LabelFrame(win, text='應檢人資料')
group.pack(padx=10,pady=10)
bdata=[
        ['姓名','蔡庠榮','術科測試編號','11101123'],
        ['座號','99','考試日期','2025-03-14']
]
for rowN in range(2):
    for columnN in range(4):
        t=tk.Label(group, text=bdata[rowN][columnN])
        t.grid(row=rowN, column=columnN)

with open('c:/test/1060302.sm') as f:
    data=f.readline()

result=''
n=int(data)
i=1
while i<=n:
    j=1
    while j<=i:
        result+=str(j)
        j+=1
    result+='\n'
    i+=1
result='第二題解果:' + '\n' + result
result2_label=tk.Label(win,text=result,justify='left')
result2_label.pack()


win.mainloop()