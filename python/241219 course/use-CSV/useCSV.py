import csv
import matplotlib.pyplot as plt

# 使用原始字符串來打開 CSV 檔案
file = open(r"d:\code\python\241219 course\use-CSV\data.csv", encoding="utf-8")
reader = csv.reader(file)
header = next(reader)
print(header)

mide = []
manny = []


for data in reader:
    print(data)
    mide.append(str(data[0]))
    manny.append(float(data[1]))

file.close()

plt.rc('font', family='microsoft jhenghei')

plt.bar(mide, manny, color=['blue','pink','black','orange'])

plt.legend()

plt.show()