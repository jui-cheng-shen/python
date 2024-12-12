import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft JhengHei')  # 設定字型

# 繪製圖表
plt.plot([1, 2, 3], [2, 4, 2], label="第一組")  # 畫出圖表，x 軸數據為 [1, 2, 3]，y 軸數據為 [2, 4, 2]
plt.plot([1, 2, 3], [1, 6, 3], label="第二組")  # 畫出圖表，x 軸數據為 [1, 2, 3]，y 軸數據為 [1, 6, 3]

# 顯示圖表標籤
plt.legend()

# 顯示圖表
plt.show()
plt.legend() #顯示圖表標籤
