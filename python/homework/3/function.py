#画二次函数
import turtle
x = -300
turtle.speed(0)

turtle.goto(-300,0)
turtle.goto(300,0)
turtle.goto(0,0)
turtle.goto(0,-300)
turtle.goto(0,300)
turtle.goto(0,0)

turtle.penup()
turtle.goto(x,x*x/300)
turtle.pendown()

step = 1
for i in range(600):
    x += step
    turtle.goto(x,x*x/300)

turtle.done()