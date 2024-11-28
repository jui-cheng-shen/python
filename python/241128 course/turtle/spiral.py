import turtle

screen=turtle.Screen()
screen.setup(500,400)
screen.bgcolor('lightblue') #背景顏色

myTurtle=turtle.Turtle()
myTurtle.color('blue')
myTurtle.shape('turtle')

myTurtle.penup()
for step in range(5,60,2):
    myTurtle.stamp()
    myTurtle.forward(step)
    myTurtle.right(24)
    
screen.mainloop() # 畫完之後不要關掉視窗