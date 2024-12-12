import matplotlib.pyplot as plt
import csv

file=open("data.csv", encoding='utf-8')
reader=csv.reader(file)
header=next(reader)#讀取第一行
print("第一行:",header)
x=[]
y=[]
for row in reader:
    print("每一列資料:",row)
    x.append(row[0])
    y.append(row[1])
    
file.close()

#繪製圖表
plt.plot(x,y,label="資料")

plt.plot(x,y)
plt.xlabel("x軸")
plt.ylabel("y軸")

#顯示圖表標籤
plt.legend()

plt.show()
