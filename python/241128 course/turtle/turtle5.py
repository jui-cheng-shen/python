import turtle

screen=turtle.Screen()
screen.setup(400,300)

myTurtle=turtle.Turtle()
myTurtle.color('red','yellow')  
myTurtle.speed(10) #速度
myTurtle.backward(100)

myTurtle.begin_fill() #開始填充
for i in range(36):
    myTurtle.forward(200)
    myTurtle.left(170)
myTurtle.end_fill() #結束填充   

screen.mainloop() # 畫完之後不要關掉視窗