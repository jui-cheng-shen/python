import pandas as pd

data=pd.Series([10,30,15])

condition=data>15 #這行程式碼會產生一個布林值的序列

print(condition) #印出布林值的序列,當data中的元素大於15時,對應的布林值為True,否則為False

filteredData=data[condition] #這行程式碼會將data中對應的布林值為True的元素篩選出來
print(filteredData)