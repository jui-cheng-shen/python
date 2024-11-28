from turtle import *

shape('turtle') #shape('turtle') 會讓畫筆變成烏龜的形狀
col=['orange','red','blue','green','gray','black','yellow']
for j in range(12):
    
    for i in range(3):
        color(col[i])
        forward(100)
        right(360/3)
    right(360/12)

done() # 畫完之後不要關掉視窗